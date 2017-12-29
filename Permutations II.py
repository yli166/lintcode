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

        for ind, val in enumerate(nums):
            if ind - 1 >= 0 and val == nums[ind - 1]: continue
            self.get_permute(nums[:ind] + nums[ind + 1:], current + [val], result)
