import copy
class Solution:
    """
    @param: source : A string
    @param: target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source, target):
        indices = {}
        for char in target:
            indices[char] = []
        miss = list(target)
        start = 0
        end = len(source)
        for i in range(len(source)):
            if source[i] in target:
                if source[i] not in miss and indices[source[i]] != []:
                    indices[source[i]].pop(0)
                elif source[i] in miss:
                    miss.remove(source[i])
                indices[source[i]].append(i)
            if miss == []:
                maximum = max([x[-1] for x in indices.values()])
                minimum = min([x[0] for x in indices.values()])
                if maximum-minimum+1 < end-start+1:
                    start = minimum
                    end = maximum
        if miss != []:
            return ""
        else:
            return source[start:end+1]