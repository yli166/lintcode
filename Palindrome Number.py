class Solution:
    """
    @param: num: a positive number
    @return: true if it's a palindrome or false
    """

    def isPalindrome(self, num):

        num = str(num)

        if not num:
            return False

        for i in range(len(num)):
            if num[i] != num[-1 - i]:
                return False

        return True    