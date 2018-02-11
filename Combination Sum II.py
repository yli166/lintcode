class Solution:
    """
    @param: num: Given the candidate numbers
    @param: target: Given the target number
    @return: All the combinations that sum to target
    """

    def __init__(self):
        self.output = []

    def combinationSum2(self, num, target):
        num.sort()
        self.dfs(num, target, 0, [])
        return self.output

    def dfs(self, nums, target, index, path):
        if target < 0:
            return  # backtracking
        if target == 0:
            self.output.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, target - nums[i], i + 1, path + [nums[i]])