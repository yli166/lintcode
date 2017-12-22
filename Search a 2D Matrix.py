class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # if len(matrix) == 0:
        #     return False

        # n, m = len(matrix), len(matrix[0])
        # start, end = 0, n * m - 1
        # while start + 1 < end:
        #     mid = (start + end) / 2
        #     x, y = mid / m, mid % m
        #     if matrix[x][y] < target:
        #         start = mid
        #     else:
        #         end = mid
        # x, y = start / m, start % m
        # if matrix[x][y] == target:
        #     return True

        # x, y = end / m, end % m
        # if matrix[x][y] == target:
        #     return True

        # return False
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False