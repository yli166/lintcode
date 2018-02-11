class Solution:
    """
    @param: n: Given the range of numbers
    @param: k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
       ans = []

       stack = []

       x = 1

       while True:

           len_stack = len(stack)

           if len_stack == k:

                ans.append(stack[:])

           if len_stack == k or x > n - k + len_stack + 1:

                if not stack:

                    return ans

                x = stack.pop() + 1

           else:

                stack.append(x)

                x += 1

        #recursion

       # def __init__(self):
       #     self.res = []
       #
       # def combine(self, n, k):
       #     self.dfs(range(1, n + 1), k, 0, [])
       #     return self.res
       #
       # def dfs(self, nums, k, index, path):
       #     # if k < 0:  #backtracking
       #     # return
       #     if k == 0:
       #         self.res.append(path[:])
       #         return  # backtracking
       #     for i in range(index, len(nums)):
       #         self.dfs(nums, k - 1, i + 1, path + [nums[i]])