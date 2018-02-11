class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # if not triangle:
        #     return
        # res = [[0 for i in xrange(len(row))] for row in triangle]
        # res[0][0] = triangle[0][0]
        # for i in xrange(1, len(triangle)):
        #     for j in xrange(len(triangle[i])):
        #         if j == 0:
        #             res[i][j] = res[i-1][j] + triangle[i][j]
        #         elif j == len(triangle[i])-1:
        #             res[i][j] = res[i-1][j-1] + triangle[i][j]
        #         else:
        #             res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
        # return min(res[-1])

        # åçç®

        end = len(triangle) - 1
        last = triangle[end]
        new_last = []
        while end > 0:
            for i, each in enumerate(triangle[end - 1]):
                new_last.append(each + min(last[i], last[i + 1]))
            last = new_last
            new_last = []
            end -= 1

        return last[0]