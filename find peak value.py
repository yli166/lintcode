class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        # write your code here




        # for i in range(1,len(A) - 1):

        #     if A[i] > A[i - 1] and A[i] > A[i + 1]:
        #         return i


        start = 1

        end = len(A) - 2

        while start + 1 < end:

            mid = (start + end) / 2

            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid

        if A[start] < A[end]:
            return end
        else:
            return start