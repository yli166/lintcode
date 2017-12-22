class Solution:
    """
    @param: n: the integer to be reversed
    @return: the reversed integer
    """

    def reverseInteger(self, n):
        # write your code here
        if n == 0:
            return 0
        neg = 1

        if n < 0:
            n = -n
            neg = - 1
        res = 0

        while n > 0:
            result = n % 10

            res = res * 10 + result

            n = n // 10

        res = res * neg

        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0
        return res