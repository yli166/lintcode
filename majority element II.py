class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    """
    #这种投票法先将第一个数字假设为众数，然后把计数器设为1，比较下一个数和此数是否相等，若相等则计数器加一，反之减一。然后看此时计数器的值，若为零，则将当前值设为候选众数。
    #这么苛刻的限制条件只有一种方法能解了，那就是摩尔投票法 Moore Voting，这种方法在之前那道题Majority Element 求众数中也使用了。
    # 题目中给了一条很重要的提示，让我们先考虑可能会有多少个众数，经过举了很多例子分析得出，任意一个数组出现次数大于n/3的众数最多有两个，具体的证明我就不会了，我也不是数学专业的。
    # 那么有了这个信息，我们使用投票法的核心是找出两个候选众数进行投票，需要两遍遍历，第一遍历找出两个候选众数，第二遍遍历重新投票验证这两个候选众数是否为众数即可
    def majorityNumber(self, nums):
        candidate1, count1 = None, 0
        candidate2, count2 = None, 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                count1 += 1
                candidate1 = num
            elif count2 == 0:
                count2 += 1
                candidate2 = num
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

        return candidate1 if count1 > count2 else candidate2