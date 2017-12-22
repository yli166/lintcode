class Solution:
    """
    @param: nums: An array of integers
    @return: An integer
    """

    def maxProduct(self, nums):
        # write your code here

        if len(nums) == 1 or len(nums) == 0:
            return nums[0]

        # maxproduct = 1
        # minproduct = 1
        # n = 0
        # product = 1

        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         n = 0
        #         minproduct = 1
        #         product = 1
        #         continue
        #     product *= nums[i]

        #     if nums[i] < 0 and n % 2 == 0:
        #         n += 1
        #         maxproduct = max(maxproduct, product / minproduct)
        #         minproduct = min(minproduct,product)
        #         continue

        #     if nums[i] < 0 and n % 2 == 1:
        #         n += 1
        #         maxproduct = max(maxproduct,product)
        #         minproduct = 1
        #         continue
        #     if nums[i] > 0 and n % 2 == 1:
        #         maxproduct = max(maxproduct, product / minproduct)
        #     if nums[i] > 0 and n % 2 == 0:
        #         maxproduct = max(maxproduct,product)

        # return maxproduct

        neg, pos, maxp = 1, 1, 0

        for each in nums:
            if each <= 0:
                neg, pos = (min(each, pos * each), neg * each)
            if each > 0:
                neg, pos = (neg * each, max(each, pos * each))
            maxp = max(maxp, pos)

        return maxp