import sys


class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers
    """

    def nextPermutation(self, nums):
        #     # write your code here

        #     for i in range(len(nums)-2, -1, -1):
        #         if nums[i] < nums[i+1]:
        #             break
        #     else:
        #         nums.reverse()
        #         return nums
        #     for j in range(len(nums)-1, i, -1):
        #         if nums[j] > nums[i]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             break
        #     for j in range(0, (len(nums) - i)//2):
        #         nums[i+j+1], nums[len(nums)-j-1] = nums[len(nums)-j-1], nums[i+j+1]
        #     return nums
        right = len(nums) - 1
        while nums[right] <= nums[right - 1] and right - 1 >= 0:
            right -= 1
        if right == 0:
            test = nums.reverse()
            return test

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        else:
            nums.reverse()
            return nums
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        k = nums[i:]
        k.sort()
        nums[i:] = k

        return nums