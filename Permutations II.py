class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        result = []
        nums.sort()
        self.get_permute(nums, [], result)
        return result

    def get_permute(self, nums, current, result):
        if not nums:
            result.append(current)

        for i in range(len(nums)):
            if i >  0 and nums[i] == nums[i -1]:
                continue
            self.get_permute(nums[:i] + nums[i + 1:],current + [nums[i]],result)
