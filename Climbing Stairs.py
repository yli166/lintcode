class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):

        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # def climbStairs(self, n):
        #     if n == 0:
        #         return 0
        #     if n == 1:
        #         return 1
        #     a, b = 1, 2
        #     for i in xrange(2, n):
        #         tmp = b
        #         b = a+b
        #         a = tmp
        #     return b