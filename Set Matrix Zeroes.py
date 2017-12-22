class Solution:
    """
    @param: matrix: A lsit of lists of integers
    @return:
    """

    def setZeroes(self, matrix):
        # write your code here

        if len(matrix) == 0:
            return
        row = len(matrix)
        col = len(matrix[0])

        row = [False for i in range(row)]
        col = [False for i in range(col)]

        for i in range(len(row)):
            for j in range(len(col)):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in range(len(row)):
            for j in range(len(col)):
                if row[i] or col[j]:
                    matrix[i][j] = 0