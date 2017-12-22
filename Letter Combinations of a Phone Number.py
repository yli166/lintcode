class Solution:
    """
    @param: digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        # write your code here

        mapping = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']
                   }


        digits = list(digits)
        F = []
        s = []

        while len(digits) > 0:
            digit = digits.pop()
            if F == []:
                for each in mapping[digit]:
                    F.append(each)
                continue

            for i in F:
                for each in mapping[digit]:
                    s.append(each + i)
            F = s
            s = []

        return F

        # 递归
        # if len(digits) == 0:
        #     return []
        # if len(digits) == 1:
        #     return list(mapping[digits[0]])

        # prev = self.letterCombinations(digits[:-1])
        # additional = mapping[digits[-1]]

        # return [s + c for s in prev for c in additional]