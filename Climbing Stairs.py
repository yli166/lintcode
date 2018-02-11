class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    #recursion
    # def climbStairs(self, n):

        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        #
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    #DP
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        list = [0 for i in range(n)]
        list[0] = 1
        list[1] = 2
        for i in range(2,n):
            list[i] = list[i - 1] + list[i - 2]

        return list[-1]