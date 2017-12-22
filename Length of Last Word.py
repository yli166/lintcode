class Solution:
    """
    @param: s: A string
    @return: the length of last word
    """

    def lengthOfLastWord(self, s):
        # write your code here
        length = 0
        right = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                right = max(right, i + 1)

            if s[i] == ' ' and right != 0:
                length = len(s[i + 1:right])
                break

        if length == 0 and len(s) != 0:
            return len(s)

        return length
