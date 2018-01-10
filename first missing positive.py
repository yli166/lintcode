class Solution:
    """
    @param: A: An array of integers
    @return: An integer
    """

    def firstMissingPositive(self, A):
        if A == []:
            return 1

        n = len(A)
        i = 0

        while i < n:
            #这里使用while 不停的进行替换保证A[i] = A[A[i] - 1]
            while A[i] != i + 1 and A[i] <= n and A[i] > 0 and A[i] != A[A[i] - 1]:
                # 不能使用同时替换
                t = A[i]
                A[i] = A[A[i] - 1]
                A[t - 1] = t
            i += 1
        for i in range(n):
            if A[i] != i + 1:
                return i + 1
        return n + 1