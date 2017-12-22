# class Solution:
#     """
#     @param: heights: a list of integers
#     @return: a integer
#     """
#     def trapRainWater(self, heights):
#         # write your code here
#         if len(heights) <= 2:
#             return 0

#         maxH = 0
#         for i,each in enumerate(heights):
#             maxH = (maxH,each)
#             maxHLocal = i

#         Left = heights[0]
#         LeftLocal1 = 0
#         LeftLocal2 = 0
#         right = heights[-1]
#         minval = 0
#         maxval = 0
#         for i in range(0:maxHLocal):
#             if 1 < i < maxHLocal and Left >= heights[i]:
#                 minval += heights[i]
#                 LeftLocal2 += 1
#             if 1 < i < maxHLocal and Left < heights[i]:
#                 val = (LeftLocal2 - LeftLocal1)*Left - minval
#                 maxval = max(maxval,val)
#                 minval = 0
#                 Left = heights[i]
#                 LeftLocal2 += 1
#                 LeftLocal1 = i

#         heights = heights[::-1]
#         maxH = 0
#         for i,each in enumerate(heights):
#             maxH = (maxH,each)
#             maxHLocal = i
#         Left = heights[0]
#         LeftLocal1 = 0
#         LeftLocal2 = 0
#         right = heights[-1]
#         minval = 0
#         maxval = 0
#         for i in range(0:maxHLocal):
#             if 1 < i < maxHLocal and Left >= heights[i]:
#                 minval += heights[i]
#                 LeftLocal2 += 1
#             if 1 < i < maxHLocal and Left < heights[i]:
#                 val = (LeftLocal2 - LeftLocal1)*Left - minval
#                 maxval = max(maxval,val)
#                 minval = 0
#                 Left = heights[i]
#                 LeftLocal2 += 1
#                 LeftLocal1 = i


#         return maxval



class Solution:
    # @param heights: a list of integers
    # @return: an integer
    def trapRainWater(self, heights):
        # write your code here
        n = len(heights)
        if n == 0: return 0
        pos = []
        neg = []

        p = q = 0
        pos.append(p)
        while (q < n - 1):
            q += 1
            if (heights[p] <= heights[q]):
                pos.append(q)
                p = q

        p = q = n - 1;
        neg.append(p)
        while (q > 0):
            q -= 1
            if (heights[q] > heights[p]):
                neg.append(q)
                p = q

        ans = 0
        for i in xrange(len(pos) - 1):
            for j in xrange(pos[i] + 1, pos[i + 1]):
                ans += heights[pos[i]] - heights[j]
        for i in xrange(len(neg) - 1):
            for j in xrange(neg[i + 1] + 1, neg[i]):
                ans += heights[neg[i]] - heights[j]
        return ans



