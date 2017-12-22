class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """

    def myPow(self, x, n):
        # write your code here

        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        tmp = x

        while n != 0:
            if n % 2 == 1:
                ans = ans * tmp
            tmp *= tmp

            n = n / 2

        return ans