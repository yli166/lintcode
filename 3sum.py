class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, nums):
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            left, right = i + 1, length - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return res
        # def threeSum(self, numbers):
        #     # write your code here
        #     numbers.sort()
        #     total = []

        #     for i in range(len(numbers)-2):
        #         if i > 0 and numbers[i] == numbers[i-1]:
        #             continue

        #         l = i + 1
        #         r = len(numbers) - 1

        #         while l < r:
        #             s = numbers[i] + numbers[l] + numbers[r]
        #             if s > 0:
        #                 r -= 1

        #             elif s < 0:
        #                 l += 1

        #             else:
        #                 total.append(numbers[i],numbers[l],numbers[r])
        #                 while l < r and numbers[l] == numbers[l + 1]:
        #                     l += 1
        #                 while l < r and numbers[r] == numbers[r - 1]:
        #                     r -= 1

        #                 l += 1, r-= 1

        #     return total
