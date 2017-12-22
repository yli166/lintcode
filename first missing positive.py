class Solution:
    """
    @param: A: An array of integers
    @return: An integer
    """

    def firstMissingPositive(self, A):
        # write your code here
        # if A == []:
        #     return 1
        # # if len(A) == 1:
        # #     return A[0] + 1
        # n = len(A)
        # res = [0] * n

        # for i in range(len(A)):
        #     if A[i] <= 0:
        #         continue
        #     res[A[i] - 1] = A[i]


        # for i in range(len(res)):
        #     if res[i] != i + 1:
        #         return i + 1

        # return len(A) + 1

        if A == []:
            return 1

        n = len(A)
        i = 0

        while i < n:
            while A[i] != i + 1 and A[i] <= n and A[i] > 0 and A[i] != A[A[i] - 1]:
                t = A[i]
                A[i] = A[A[i] - 1]
                A[t - 1] = t
            i += 1
        for i in xrange(n):
            if A[i] != i + 1: return i + 1
        return n + 1