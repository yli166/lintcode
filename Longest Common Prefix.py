class Solution:
    """
    @param: strs: A list of strings
    @return: The longest common prefix
    """

    def longestCommonPrefix(self, strs):
        # write your code here
        # dict = {}

        # for i in range(len(strs[0])):
        #     dict[strs[0][i]] = i

        # limit

        # for each in strs:
        #     for i in strs[each]:
        #         if strs[each][i] != strs[0][i]:
        #             limit = i
        #             break

        if not strs:
            return ''
        for each in strs:
            if not each:
                return ""

        count = len(strs)
        limit = len(strs[count - 1])
        while count > 0:
            for each in range(limit):
                if strs[count - 1][each] != strs[0][each]:
                    limit = each
                    break
            count -= 1

        return strs[0][0:limit]