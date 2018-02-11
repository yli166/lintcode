class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here

        # if not nums:
        #     return [[]]

        # result = []
        # stack = [[i] for i in nums]

        # while stack:
        #     last = stack.pop()
        #     if len(last) == len(nums):
        #         result.append(last)
        #         continue

        #     for n in nums:
        #         if n not in last:
        #             stack.append(last + [n])


        # return result

        # recursion
        result = []
        nums.sort()
        self.get_permute(nums, [], result)
        return result

    def get_permute(self, nums, current, result):
        if not nums:
            result.append(current)

        for i in range(len(nums)):
            # if ind-1>=0 and val==nums[ind-1]: continue  # JUMP; only need to compare to previous value
            self.get_permute(nums[:i] + nums[i + 1:], current + [nums[i]], result)