class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1

        first = target[0]

        length = len(target)
        length2 = len(source)

        for i in range(length2 - length + 1):
            if source[i: i + length] == target[:]:
                return 1

        return -1