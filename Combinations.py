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