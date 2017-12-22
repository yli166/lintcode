class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # write your code here

        n = 0

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            nums[n] = nums[i]
            n += 1

        return n