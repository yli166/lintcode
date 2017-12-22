class Solution:
    """
    @param: A: an integer rotated sorted array
    @param: target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):

        #     # write your code here
        #     for each in range(len(A)):
        #         if A[each] == target:
        #             return each


        #     return -1


        if len(A) == 0:
            return -1

        start = 0
        low = 0
        high = len(A) - 1
        end = len(A) - 1
        if A[start] == target:
            return start
        if A[end] == target:
            return end

        # while start + 1 < end:

        #     mid = start + (end - start) / 2
        #     if A[mid] == target:
        #         return mid
        #     if A[start] < A[mid]:
        #         if A[mid] <= target and A[mid] > start:
        #             end = mid
        #         else:
        #             start = mid
        #     else:
        #         if A[mid] < target and target <= A[end]:
        #             start = mid
        #         else:
        #             end = mid


        # return -1

        while low <= high:
            mid = (low + high) / 2
            if target == A[mid]:
                return mid

            if A[low] <= A[mid]:
                if A[low] < target < A[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if A[mid] < target < A[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1