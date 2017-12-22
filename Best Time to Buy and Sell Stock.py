class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):

        if not prices:
            return 0

        low = prices[0]
        max = 0

        for i in range(len(prices)):
            if i == 0:
                continue

            if prices[i] - low > max:
                max = prices[i] - low
            if prices[i] < low:
                low = prices[i]

        return max