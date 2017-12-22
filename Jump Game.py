class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        # write your code here
        limit = A[0]
        for i in range(len(A)):
            if limit >= i:
                limit = max(limit, (i + A[i]))

        if limit >= len(A) - 1:
            return True

        return False