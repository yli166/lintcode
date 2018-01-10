class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        # k = 0
        # for i in range(len(A)):
        #     if not A[i]:
        #         A[i] = B[k]
        #         k += 1
        #
        # A.sort()
        # return A

        while m > 0 and n > 0:
            if A[m-1] >= B[n-1]:
                A[m+n-1] = A[m-1]
                m -= 1
            else:
                A[m+n-1] = B[n-1]
                n -= 1
        if n > 0:
            A[:n] = B[:n]
