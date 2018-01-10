class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        dict = {0: -1}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum in dict:
                return[dict[sum] + 1, i]
            dict[sum] = i