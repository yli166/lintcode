class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        # sum = 0

        # minsum = 0
        # maxsum = 0

        # for i in range(1,len(prices)):
        #     sum +=  prices[i] - prices[i - 1]

        #     if sum - minsum > maxsum:
        #         maxsum = sum - minsum

        #     if sum <= minsum:
        #         minsum = sum

        # return maxsum
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))