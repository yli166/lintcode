class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """

    def removeElement(self, A, elem):
        start = 0
        end = len(A) - 1

        while start <= end:
            if A[start] == elem:
                A[start], A[end], end = A[end], A[start], end - 1
            else:
                start += 1
        return start