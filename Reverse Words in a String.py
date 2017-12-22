class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        s = s.strip().split()
        s = s[::-1]
        s = ' '.join(s)
        return s