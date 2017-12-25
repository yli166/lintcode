import collections


class Solution:
    """
    @param: n: An integer
    @return: a square matrix
    """

    def generateMatrix(self, n):
        # 终止条件是 count = n*n
        length = n - 1

        matrix = [[0 for i in range(n)] for j in range(n)]
        direct = 0
        up = 0
        down = length
        left = 0
        right = length
        count = 0

        while True:
            if direct == 0:
                for i in range(left, right + 1):
                    count += 1
                    matrix[up][i] = count
                up += 1
            if direct == 1:
                for i in range(up, down + 1):
                    count += 1
                    matrix[i][right] = count
                right -= 1
            if direct == 2:
                for i in range(right, left - 1, -1):
                    count += 1
                    matrix[down][i] = count
                down -= 1
            if direct == 3:
                for i in range(down, up - 1, -1):
                    count += 1
                    matrix[i][left] = count
                left += 1
            if count == n ** 2:
                return matrix

            direct = (direct + 1) % 4 