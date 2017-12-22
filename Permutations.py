class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here

        if not nums:
            return [[]]

        result = []
        stack = [[i] for i in nums]

        while stack:
            last = stack.pop()
            if len(last) == len(nums):
                result.append(last)
                continue

            for n in nums:
                if n not in last:
                    stack.append(last + [n])

        return result