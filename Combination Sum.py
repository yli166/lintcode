class Solution:
    """
    @param: candidates: A list of integers
    @param: target: An integer
    @return: A list of lists of integers
    """

    def __init__(self):
        self.output = []

    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [])
        return self.output

    def dfs(self, nums, target, index, path):
        if target < 0:
            return  # backtracking
        if target == 0:
            self.output.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]])


