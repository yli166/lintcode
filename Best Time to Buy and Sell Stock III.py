class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        result1 = self.profit(prices)
        left, right = result1[0], result1[1]

        r1 = self.profit(prices[:left])[-1] + result1[-1]
        r2 = self.profit(prices[right + 1:])[-1] + result1[-1]
        r3 = result1[-1] - self.loss(prices[left + 1: right])

        return max(r1, r2, r3)

    def profit(self, prices):

        n = len(prices)
        if n < 2:
            return [0, 0, 0]

        sum_val, max_val = 0, 0
        left, right = 0, 1
        temp = left

        for i in range(n - 1):

            sum_val += prices[i + 1] - prices[i]

            if sum_val > max_val:
                right = i + 1
                left = temp
                max_val = sum_val

            sum_val = max(0, sum_val)
            if sum_val == 0:
                temp = i + 1

        return [left, right, max_val]

    def loss(self, prices):

        n = len(prices)
        if n < 2:
            return 0

        sum_val, min_val = 0, 0

        for i in range(n - 1):
            sum_val += prices[i + 1] - prices[i]
            min_val = min(min_val, sum_val)
            sum_val = min(0, sum_val)

        return min_val

    # def maxProfit(self, prices):
    #     length = len(prices)
    #     if length == 0: return 0
    #     f1 = [0 for i in range(length)]
    #     f2 = [0 for i in range(length)]
    #
    #     minV = prices[0];
    #     f1[0] = 0
    #     for i in range(1, length):
    #         minV = min(minV, prices[i])
    #         f1[i] = max(f1[i - 1], prices[i] - minV)
    #
    #     maxV = prices[length - 1];
    #     f2[length - 1] = 0
    #     for i in range(length - 2, -1, -1):
    #         maxV = max(maxV, prices[i])
    #         f2[i] = max(f2[i + 1], maxV - prices[i])
    #
    #     res = 0
    #     for i in range(length):
    #         if f1[i] + f2[i] > res: res = f1[i] + f2[i]
    #     return res