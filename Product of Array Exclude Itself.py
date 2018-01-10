class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        if len(nums) == 1:
            return [1]
        B = []
        length = len(nums)
        for i in range(length):
            mul = 1
            for j in range(length):

                if i == j:
                    continue
                mul *= nums[j]
            B.append(mul)

        return B