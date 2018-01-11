class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # 快慢指针 遇到相同值则跳过
        slow = 0
        fast = 0
        if len(nums) == 1:
            return nums[0]

        while fast < len(nums):
            if fast < len(nums) - 1 and nums[fast] == nums[fast + 1]:
                fast += 1
            else:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                fast += 1
                slow += 1

        return slow