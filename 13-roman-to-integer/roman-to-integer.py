class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = [0] * 26  # For all uppercase letters
        values[ord('I') - 65] = 1
        values[ord('V') - 65] = 5
        values[ord('X') - 65] = 10
        values[ord('L') - 65] = 50
        values[ord('C') - 65] = 100
        values[ord('D') - 65] = 500
        values[ord('M') - 65] = 1000

        total = 0
        prev = 0

        for i in range(len(s) - 1, -1, -1):
            val = values[ord(s[i]) - 65]
            total += val if val >= prev else -val
            prev = val

        return total

        