class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        res = []
        cycleLen = 2 * numRows - 2

        for r in range(numRows):
            for i in range(r, len(s), cycleLen):
                res.append(s[i])
                # Middle rows- add the upward diagonal element
                j = i + cycleLen - 2 * r
                if r != 0 and r != numRows - 1 and j < len(s):
                    res.append(s[j])

        return "".join(res)
