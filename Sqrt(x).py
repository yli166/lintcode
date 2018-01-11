class Solution:
    """
    @param: x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        #     start = 1
        #     end = x
        #     while start + 1 < end:
        #         mid = start + (end - start) / 2
        #         if mid * mid == x:
        #             return mid
        #         if mid * mid > x:
        #             end = mid
        #         if mid * mid < x:
        #             start = mid
        #     if end * end <= x:
        #         return end
        #     return start

        start = 1
        end = x
        while start <= end:
            mid = (start + end) / 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                start = mid + 1
            if mid * mid > x:
                end = mid - 1
        if end * end <= x:
            return end
        return start