class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        if len(nums) == 0 or not nums:
            return nums

        maxsum = nums[0]
        minsum = 0
        sum = 0

        for num in nums:

            sum += num

            if sum - minsum > maxsum:
                maxsum = sum - minsum
            if sum < minsum:
                minsum = sum

        return maxsum