class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        sum = 0
        dp = [0 for i in range(m + 1)]
        dp[0] = 1
        for i in A:
            for j in range(m, -1, -1):
                if j - i >= 0 and dp[j - i] > 0:
                    sum = max(sum, j)
                    dp[j] = 1

        return sum