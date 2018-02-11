class Solution:
    """
    @param: nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):

        if nums is None or not nums:
            return 0
        dp = [1] * len(nums)

        for cur, i in enumerate(nums):
            for j in range(cur):
                if nums[j] < i:
                    dp[cur] = max(dp[cur], dp[j] + 1)

        return max(dp)