class Solution:
    """
    @param: s: Roman representation
    @return: an integer
    """

    def romanToInt(self, s):
        # write your code here
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        intial = 0

        for i in range(len(s)):
            if i > 0 and map[s[i]] > map[s[i - 1]]:
                intial += map[s[i]] - 2 * map[s[i - 1]]
            else:
                intial += map[s[i]]

        return intial
