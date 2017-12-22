class Solution:
    """
    @param: tokens: The Reverse Polish Notation
    @return: the value
    """

    def evalRPN(self, tokens):
        # write your code here

        A = []

        for each in tokens:
            if each == '+':
                x1 = A.pop()
                x2 = A.pop()
                result = x1 + x2
                A.append(result)
                continue
            elif each == '-':
                x1 = A.pop()
                x2 = A.pop()
                result = x2 - x1
                A.append(result)
                continue
            elif each == '*':
                x1 = A.pop()
                x2 = A.pop()
                result = x2 * x1
                A.append(result)
                continue
            elif each == '/':
                x1 = A.pop()
                x2 = A.pop()
                result = x2 * 1.0 / x1     #考虑小数的情况
                A.append(int(result))       #将小数化为整数
                continue

            A.append(int(each))

        return A.pop()