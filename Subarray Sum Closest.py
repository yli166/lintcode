import sys
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        dict = {0:-1}
        sum = 0
        min = sys.maxsize
        for each in range(len(nums)):
            sum += nums[each]
            for i in dict:
                if i == sum:
                    return [dict[i] + 1, each]
                if abs(sum - i) < min:
                    min = abs(sum - i)
                    local = [dict[i] + 1,each]
            dict[sum] = each
        return local