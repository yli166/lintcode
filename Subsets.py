class Solution:
    """
    @param: nums: A set of numbers
    @return: A list of lists
    """

    # iteratively
    def subsets(self, nums):
        # write your code here

        if not nums:
            return [[]]

        if len(nums) == 1:
            return [[], nums]
        nums.sort()
        result = [[], [nums[0]]]
        new_result = []
        for each in nums[1::]:
            for i in result:
                new_result.append(i + [each])
            result += new_result
            new_result = []

        return result

        # recursively

        #     def search(self,nums,S,index):
        #         if index == len(nums):
        #             return self.result.append(S)

        #         return self.search(nums,S + [nums[index]], index + 1), self.search(nums,S,index + 1)
        #     def subsets(self, nums):
        #         self.result = []
        #         self.search(sorted(nums), [], 0)
        #         return self.result