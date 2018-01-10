class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: The length of longest common subsequence of A and B
    """

    def longestCommonSubsequence(self, A, B):
        matrix = [[0 for i in range(len(A) + 1)] for j in range(len(B) + 1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    matrix[i + 1][j + 1] = matrix[i][j] + 1
                else:
                    matrix[i + 1][j + 1] = max(matrix[i + 1][j], matrix[i][j + 1])

        return matrix[-1][-1]