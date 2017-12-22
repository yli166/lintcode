class Solution:
    """
    @param: num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, num):
        # write your code here


        hashmap = {}

        for each in num:
            hashmap[each] = True

        max_n = 0

        for k, v in hashmap.items():
            if not v:
                continue

            left = k - 1
            right = k + 1

            while left in hashmap and hashmap[left]:
                hashmap[left] = False
                left -= 1

            while right in hashmap and hashmap[right]:
                hashmap[right] = False
                right += 1

            n = right - left - 1

            max_n = max(max_n, n)

        return max_n

# 使用哈希表 将检索过的left right 标记为 False 并更新 left - 1 和 right - 1