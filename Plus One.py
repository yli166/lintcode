class Solution:
    """
    @param: digits: a number represented as an array of digits
    @return: the result
    """

    def plusOne(self, digits):
        digits = digits[::-1]

        digits[0] += 1

        for i in range(len(digits)):
            if digits[i] == 10 and i < len(digits) - 1:
                digits[i] = 0
                digits[i + 1] += 1
            if digits[i] == 10 and i == len(digits) - 1:
                digits[i] = 0
                digits.append(1)

        digits = digits[::-1]

        return digits


        # 递归
        # def plusOne(self, digits):
        #     digits = digits or [0]
        #     last = digits.pop()

        #     if last == 9:
        #         return self.plusOne(digits) + [0]
        #     else:
        #         return digits + [last + 1]