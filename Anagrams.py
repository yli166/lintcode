class Solution:
    """
    @param: strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):

        # sw = ''.join(sorted())

        # # test = []
        # # test[0] = ''.join(sorted(strs[0]))
        dict = {}
        target = []
        target2 = []

        for each in strs:
            test = ''.join(sorted(each))
            if test not in dict:
                dict[test] = 1
            else:
                dict[test] += 1

        for each in dict:
            if dict[each] > 1:
                target.append(each)

        for each in strs:
            test = ''.join(sorted(each))
            if test in target:
                target2.append(each)

        return target2

# class Solution:
#     # @param strs: A list of strings
#     # @return: A list of strings
#     def anagrams(self, strs):
#         # write your code here
#         dict = {}
#         for word in strs:
#             sortedword = ''.join(sorted(word))
#             dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
#         res = []
#         for item in dict:
#             if len(dict[item]) >= 2:
#                 res += dict[item]
#         return res