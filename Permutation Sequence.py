class Solution:
    """
    @param: n: n
    @param: k: the k th permutation
    @return: return the k-th permutation
    """

    def getPermutation(self, n, k):
        nums = [i for i in range(1, n + 1)]
        count = 1
        while count < k:
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    break
            else:
                nums.reverse()
                count += 1
                continue

            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break

            nums[i + 1:] = sorted(nums[i + 1:])
            count += 1
        num = [str(i) for i in nums]
        num = ''.join(num)
        return num