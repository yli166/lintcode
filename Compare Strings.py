class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        dict = {}
        for i in A:
            dict[i] = dict.get(i,0) + 1
        for i in B:
            dict[i] = dict.get(i,0) - 1
        for i in dict:
            if dict[i] < 0:
                return False
        return True