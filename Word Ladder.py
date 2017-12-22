import collections


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):

        # def ladderLength(self, start, end, dict):
        #     # write your code here
        #     dict.append(end)

        #     length = len(start)

        #     result = []
        #     for i in range(length):
        #         if start[i] == end[i]:
        #             continue
        #         result.append(i)

        #     length2 = len(result)

        #     if result == []:
        #         return 0



        #     current = start

        #     for i in result:
        #         current  = list(current)
        #         end = list(end)
        #         current[i] = end[i]
        #         current = ''.join[current]

        dict.add(end)
        wordLen = len(start)
        queue = collections.deque([(start, 1)])   #双向队列
        while queue:
            curr = queue.popleft()
            currWord = curr[0]
            currLen = curr[1]
            if currWord == end: return currLen
            for i in range(wordLen):
                part1 = currWord[:i]
                part2 = currWord[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currWord[i] != j:
                        nextWord = part1 + j + part2
                        if nextWord in dict:
                            queue.append((nextWord, currLen + 1))
                            dict.remove(nextWord)
        return 0