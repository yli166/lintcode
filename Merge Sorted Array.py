class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        k = 0
        for i in range(len(A)):
            if not A[i]:
                A[i] = B[k]
                k += 1

        A.sort()
        return A