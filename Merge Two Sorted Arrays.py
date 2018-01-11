class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        ans = []
        a = 0
        b = 0
        while a < len(A) and b < len(B):
            if A[a] < B[b]:
                ans.append(A[a])
                a += 1
            elif A[a] > B[b]:
                ans.append(B[b])
                b += 1
            else:
                ans.append(A[a])
                ans.append(B[b])
                a += 1
                b += 1
        while a < len(A):
            ans.append(A[a])
            a += 1
        while b < len(B):
            ans.append(B[b])
            b += 1
        return ans