class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                while nums[mid] == nums[mid - 1]:
                    mid -= 1
                return mid
            if nums[mid] < target:
                start = mid + 1
            if nums[mid] > target:
                end = mid - 1
        return -1