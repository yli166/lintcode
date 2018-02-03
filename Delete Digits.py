class Solution:
    """
    @param: A: A positive integer which has N digits, A is a string
    @param: l: Remove k digits
    @return: A string
    """

    def DeleteDigits(self, A, l):
        A = list(A)
        while l > 0:
            F = True
            for i in range(len(A) - 1):
                if A[i] > A[i + 1]:
                    del A[i]
                    F = False
                    break
            if F and len(A) > 1:
                A.pop()
            l -= 1

        while len(A) > 1 and A[0] == '0':
            del A[0]
        return ''.join(A)