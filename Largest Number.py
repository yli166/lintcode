class Solution:
    """
    @param: nums: A list of non negative integers
    @return: A string
    """

    def largestNumber(self, nums):
        # write your code here

        comp = lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0
        nums = map(str, nums)
        nums.sort(cmp=comp, reverse=True)
        return str(int("".join(nums)))
