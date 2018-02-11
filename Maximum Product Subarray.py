class Solution:
    """
    @param: nums: An array of integers
    @return: An integer
    """

    def maxProduct(self, nums):
        # write your code here

        if len(nums) == 1 or len(nums) == 0:
            return nums[0]
        if not nums:
            return 0

        # res = nums[0]
        # min_p = max_p = nums[0]
        # for i in xrange(1, len(nums)):
        #     tmp = min_p
        #     min_p = min(nums[i], min_p * nums[i], max_p * nums[i])
        #     max_p = max(nums[i], max_p * nums[i], tmp * nums[i])
        #     res = max(res, max_p)
        # return res

        neg, pos, maxp = 1, 1, 0

        for each in nums:
            if each <= 0:
                neg, pos = (min(each, pos * each), neg * each)
            if each > 0:
                neg, pos = (neg * each, max(each, pos * each))
            maxp = max(maxp, pos)

        return maxp