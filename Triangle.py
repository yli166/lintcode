class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        # sum = 0
        # for i in triangle:
        #     test = i[0]
        #     for j in i:
        #         test = min(test, j)

        #     sum += test

        # return sum

        # if len(triangle) == 1:
        #     return triangle[0][0]

        # position = 0
        # start = 0
        # end = len(triangle)
        # sum = triangle[0][0]

        # while start < end - 1:
        #     # minvalue = min(triangle[start + 1][position],triangle[start + 1][position + 1])
        #     if triangle[start + 1][position] > triangle[start + 1][position + 1]:
        #         position += 1
        #         sum += triangle[start + 1][position + 1]
        #     else:
        #         sum += triangle[start + 1][position]

        #     start += 1

        # return sum

        # 倒着算

        end = len(triangle) - 1
        last = triangle[end]
        new_last = []
        while end > 0:
            for i, each in enumerate(triangle[end - 1]):
                new_last.append(each + min(last[i], last[i + 1]))
            last = new_last
            new_last = []
            end -= 1

        return last[0]