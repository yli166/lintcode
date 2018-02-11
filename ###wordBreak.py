class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    # def wordBreak(self, s, dict):

    #     l = 0
    #     r = 1
    #     ans = ''
    #     if len(s) == 0:
    #         if s[0] in dict:
    #             return True
    #         else:
    #             return False


    #     for i in range(len(s)):
    #         if s[l:r] in dict:
    #             l = i
    #             r = i + 1
    #             ans += s[1:r] + ' '
    #         elif r == len(s) and s[l:r] in dict:
    #             ans += s[l:r]

    #         else:
    #             r = i + 1

    #     return ans

    def wordBreak(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0

        n = len(s)
        f = [False] * (n + 1)
        f[0] = True

        maxLength = max([len(w) for w in dict])
        for i in xrange(1, n + 1):
            for j in range(1, min(i, maxLength) + 1):
                if not f[i - j]:
                    continue
                if s[i - j:i] in dict:
                    f[i] = True
                    break

        return f[n]

        # def wordBreak(self, s, dict):
        #     test = [False] * (len(s) + 1)
        #     test[0] = True
        #     for i in range(len(s)):
        #         for j in range(i,len(s)):
        #             if test[i] and s[i:j + 1] in dict:
        #                 test[j + 1] = True
        #     return test[-1]