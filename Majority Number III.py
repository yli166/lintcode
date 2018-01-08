import collections
class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        dict = {}
        max = 0
        for each in nums:
            dict[each] = dict.get(each,0) + 1
            if dict[each] > max:
                max = dict[each]
                ans = each
        return ans