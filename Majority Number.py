class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """

    def majorityNumber(self, nums):
        nums.sort()
        # write your code here
        m = len(nums) // 2

        return nums[m]