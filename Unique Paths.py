class Solution:
    """
    @param: m: positive integer (1 <= m <= 100)
    @param: n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def c(self, m, n):
        mp = {}
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0):
                    mp[(i, j)] = 1
                else:
                    mp[(i, j)] = mp[(i - 1, j)] + mp[(i, j - 1)]
        return mp[(m - 1, n - 1)]

    def uniquePaths(self, m, n):
        # write your code here
        # if m == 0 and n == 0:
        #     return 1

        # return self.uniquePaths(self,m - 1,n) + self.uniquePaths(self,n,m - 1)

        return self.c(m, n)



    #DP

    # class Solution:
    #     # @return an integer
    #     def uniquePaths(self, m, n):
    #         aux = [[1 for x in range(n)] for x in range(m)]
    #         for i in range(1, m):
    #             for j in range(1, n):
    #                 aux[i][j] = aux[i][j - 1] + aux[i - 1][j]
    #         return aux[-1][-1]