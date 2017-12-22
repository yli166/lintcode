class Solution:
    """
    @param: n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):

        # Write your code here
        d = {}
        while True:
            d[n] = 1
            n = sum([int(x) * int(x) for x in list(str(n))])
            if n == 1 or n in d:
                break
        return n == 1