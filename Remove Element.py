class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return None

        if len[nums] == 1:
            if nums[0] == val:
                return []
            else:
                return nums

        lenth = len(nums) - 1
        count = 0
        n = 0
        while count + n < len(nums):
            if nums[count] == val:
                n += 1
                nums[count:(lenth - 1)] = nums[(count + 1):lenth]
            else:
                count += 1

        return lenth - n