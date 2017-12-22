class Solution:
    """
    @param: n: The integer
    @return: Roman representation
    """
    def intToRoman(self, n):
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        intial = ''
        i = 0

        while n:
            intial += (n // values[i]) * numerals[i]
            n = n % values[i]
            i += 1

        return intial