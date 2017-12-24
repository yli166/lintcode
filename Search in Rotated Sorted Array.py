class Solution:
    """
    @param: A: an integer rotated sorted array
    @param: target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        # write your code here
        if len(A) == 0:
            return -1
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            if A[start] < A[mid]:
                if A[start] <= target and A[mid] > target:
                    end = mid
                else:
                    start = mid
            else:
                if A[end] >= target and A[mid] < target:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1