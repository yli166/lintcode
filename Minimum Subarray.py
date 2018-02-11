import sys


class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """

    def minSubArray(self, nums):
        if len(nums) == 0 or not nums:
            return nums
        sum = 0
        maxvalue = 0
        minvalue = nums[0]

        for each in nums:
            sum += each
            if sum - maxvalue < minvalue:
                minvalue = sum - maxvalue
            if sum > maxvalue:
                maxvalue = sum

        return minvalue