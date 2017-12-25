class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # if len(nums)==0:
        #     return 0
        # cur=0
        # point=0

        # while point<len(nums):
        #     if point<len(nums)-2 and nums[point]==nums[point+1] and nums[point]==nums[point+2]:
        #         point=point+1
        #     else:
        #         nums[cur]=nums[point]
        #         point=point+1
        #         cur=cur+1
        # return cur
        n = 0
        count = 0
        if len(nums) == 1:
            return nums[0]

        for i, each in enumerate(nums):
            if nums[i] == nums[i - 1]:
                count = 1
            if nums[i] != nums[i - 1]:
                n += 1
                if count == 1:
                    n += 1
                count = 0
            if i == len(nums) - 1:
                if nums[i] == nums[i - 1]:
                    n += 1
        return n