class Solution:
    """
    @param: s: A string
    @return: whether the string is a valid parentheses
    """

    def isValidParentheses(self, s):
        # write your code here
        stack = []
        # 入栈
        for each in s:
            if each == '[' or each == '{' or each == '(':
                stack.append(each)
            else:
                # 栈需非空
                if not stack:
                    return False
                if each == ']' and stack[-1] != '[' or each == ')' and stack[-1] != '(' or each == '}' and stack[
                    -1] != '{':
                    return False
                # 弹栈

                stack.pop()

        return not stack