class Solution:
    """
    @param: matrix: A list of lists of integers
    @param: target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix == []:
            return 0
        i = len(matrix) - 1
        j = 0
        count = 0
        while True:
            if i < 0 or j > len(matrix[0]) - 1:
                break
            if matrix[i][j] == target:
                count += 1
                i -= 1
            if matrix[i][j] > target:
                i -= 1
            if matrix[i][j] < target:
                j += 1

        return count