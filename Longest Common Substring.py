class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        matrix = [[0 for i in range(len(A) + 1)] for j in range(len(B) + 1)]
        max = 0
        # for i in range(len(A)):
        #     for j in range(len(B)):
        #         if A[i] == B[j]:
        #             matrix[i + 1][j + 1] = matrix[i][j] + 1
        #             if matrix[i + 1][j + 1] > max:
        #                 max = matrix[i + 1][j + 1]
                        # p = i + 1
        # 如果 求lcs的实际值 就return A[p - max,p]
        return max