class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """

    def anagram(self, s, t):
        dict = {}
        for i in s:
            dict[i] = dict.get(i, 0) + 1
        for j in t:
            dict[j] = dict.get(j, 0) - 1
        for each in dict:
            if dict[each] != 0:
                return False

        return True