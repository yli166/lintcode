class Solution:
    """
    @param: x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        # write your code here
        start = 1
        end = x

        while start + 1 < end:
            mid = start + (end - start) / 2

            if mid * mid == x:
                return mid

            if mid * mid > x:
                end = mid

            if mid * mid < x:
                start = mid

        if end * end <= x:
            return end

        return start