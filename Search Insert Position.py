class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: An integer
    """

    def searchInsert(self, A, target):
        # write your code here
        if len(A) == 0 or not A:
            return 0
        start = 0
        end = len(A) - 1

        while start <= end:
            mid = (start + end) / 2
            if target == A[mid]:
                return mid
            if A[mid] < target:
                start = mid + 1
            if A[mid] > target:
                end = mid - 1

        return start