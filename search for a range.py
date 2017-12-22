class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        res = [-1, -1]
        if A == None or len(A) == 0:
            return res
        if target < A[0] or target > A[-1]:
            return res
        start = 0
        end = len(A) - 1
        left = -1
        right = -1
        if A[0] == target:
            left = 0
        else:
            while start <= end:
                mid = (start + end) / 2
                if A[mid] < target:
                    start = mid + 1
                elif A[mid] > target:
                    end = mid - 1
                elif A[mid] == target:
                    if A[mid - 1] != target:
                        left = mid
                        break
                    else:
                        end = mid - 1
        start = 0
        end = len(A) - 1
        if A[end] == target:
            right = end
        else:
            while start <= end:
                mid = (start + end) / 2
                if A[mid] < target:
                    start = mid + 1
                elif A[mid] > target:
                    end = mid - 1
                elif A[mid] == target:
                    if A[mid + 1] != target:
                        right = mid
                        break
                    else:
                        start = mid + 1

        return [left, right]