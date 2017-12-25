class Solution:
    """
    @param: A: an integer ratated sorted array and duplicates are allowed
    @param: target: An integer
    @return: a boolean
    """

    def search(self, A, target):
        # write your code here
        if len(A) == 0:
            return False

        start, end = 0, len(A) - 1
        if A[start] == target:
            return True
        if A[end] == target:
            return True
        while start + 1 < end:
            if end - 1 > start and A[end] == A[end - 1]:
                end -= 1
                continue
            if start + 1 < end and A[start] == A[start + 1]:
                start += 1
                continue
            mid = start + (end - start) / 2
            if A[mid] == target:
                return True
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

        return False