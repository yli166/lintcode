class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            return A[0]
        record = [0, A[0]]
        if n >= 2:
            for i in range(2, n + 1):
                record.append(max(record[i - 1], record[i - 2] + A[i - 1]))
        return record[-1]