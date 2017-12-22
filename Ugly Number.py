class Solution:
    """
    @param: num: An integer
    @return: true if num is an ugly number or false
    """

    def isUgly(self, num):
        # write your code here
        if num == 0:
            return False

        while True:

            if num % 2 == 0:
                num = num / 2
            elif num % 3 == 0:
                num = num / 3
            elif num % 5 == 0:
                num = num / 5
            else:
                if num == 1:
                    return True
                else:
                    return False