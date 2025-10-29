class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        cycle = 2 * numRows - 2
        res = []

        for r in range(numRows):
            for i in range(r, len(s), cycle):
                res.append(s[i])
                j = i + cycle - 2 * r
                if r != 0 and r != numRows - 1 and j < len(s):
                    res.append(s[j])

        return ''.join(res)
