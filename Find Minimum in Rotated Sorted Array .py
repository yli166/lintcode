class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        # write your code here

        if nums == 1:
            return nums[0]
        # 注意nums[0 - 1] = -1 的情况
        if nums[0] > nums[1]:
            return nums[1]

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] > nums[i]:
                return nums[i]

        return nums[0]