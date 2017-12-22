class Solution:
    """
    @param: n: An integer
    @return: An integer which is the first bad version.
    """

    def findFirstBadVersion(self, n):
        # write your code here
        start = 1
        end = n

        while start + 1 < end:
            mid = (start + end) / 2
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid

        if SVNRepo.isBadVersion(start):
            return start

        return end