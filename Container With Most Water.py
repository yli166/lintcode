class Solution:
    """
    @param: heights: a vector of integers
    @return: an integer
    """
    # time exceed
    # def maxArea(self, heights):
    #     # write your code here
    #
    #     maxarea = 0
    #
    #     for i, h in enumerate(heights[:-1]):
    #         I = i + 1
    #         for H in heights[i + 1:]:
    #             minheight = min(h, H)
    #
    #             area = minheight * (I - i)
    #
    #             maxarea = max(maxarea, area)
    #
    #             I += 1
    #
    #     return maxarea


    def maxArea(self, heights):
        # write your code here
        if not heights:
            return 0

        left = 0
        right = len(heights) - 1
        maxvalue = min(heights[left], heights[right]) * (right - left)
        maxarea = 0
        while right > left:
            if heights[right] > heights[left]:
                maxarea = max(maxarea, min(heights[left], heights[right]) * (right - left))
                left += 1
            else:
                maxarea = max(maxarea, min(heights[left], heights[right]) * (right - left))
                right -= 1

        return maxarea
