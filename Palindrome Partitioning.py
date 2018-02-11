class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def __init__(self):
        self.res = []

    def partition(self, s):
        self.dfs(s, [])
        return self.res

    def dfs(self, s, path):
        if not s:
            self.res.append(path[:])
            return
        for i in range(len(s)):
            if self.ispar(s[:i + 1]):
                self.dfs(s[i + 1:], path + [s[:i + 1]])

    def ispar(self, s):
        return s == s[::-1]
