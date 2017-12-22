class Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """

    def jump(self, A):
        # write your code here
        limit = A[0]
        count = 1
        for i in range(len(A) - 1):
            if limit >= i and limit < len(A):
                cur = limit
                limit = max(limit, i + A[i])
                if cur != limit:
                    count += 1

        return count
