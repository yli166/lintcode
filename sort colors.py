class Solution:
    """
    @param: nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """

    def sortColors(self, nums):
        # write your code 
        # dict = {0:0,1:0,2:0}
        # for each in nums:
        #     if each == 0:
        #         dict[each] += 1
        #     if each == 1:
        #         dict[each] += 1
        #     if each == 2:
        #         dict[each] += 1

        # nums = [0]*dict[0] + [1]*dict[1] + [2]*dict[2]
        # return nums

        if not nums or len(nums) == 0:
            return

        i, left, right = 0, 0, len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1