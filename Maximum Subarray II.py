class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def maxTwoSubArrays(self, nums):
        if len(nums) == 0:
            return 0

        f1 = [0 for i in nums]
        f2 = [0 for i in nums]

        maxvalue = nums[0]
        f1[0] = nums[0]
        if nums[0] >= 0:
            minvalue = 0
        else:
            minvalue = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            sum += nums[i]
            if sum - minvalue > maxvalue:
                maxvalue = sum - minvalue
            if sum < minvalue:
                minvalue = sum
            f1[i] = max(f1[i - 1], maxvalue)

        maxvalue = nums[-1]
        f2[-1] = nums[-1]
        if nums[-1] >= 0:
            minvalue = 0
        else:
            minvalue = nums[-1]
        sum = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            sum += nums[i]
            if sum - minvalue > maxvalue:
                maxvalue = sum - minvalue
            if sum < minvalue:
                minvalue = sum
            f2[i] = max(f2[i + 1], maxvalue)
        res = f1[0] + f2[1]
        for i in range(len(nums) - 1):
            res = max(res, f1[i] + f2[i + 1])

        return res