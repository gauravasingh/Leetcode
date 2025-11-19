class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Total happy strings
        total = 3 * (2 ** (n - 1))
        if k > total:
            return ""
        
        res = []
        prev = ''
        chars = ['a', 'b', 'c']
        
        # At each step choose lexicographically
        for pos in range(n):
            for c in chars:
                if c == prev:
                    continue
                # No of happy strings formed if we pick char c at this position
                count = 2 ** (n - pos - 1)
                if k > count:
                    k -= count
                else:
                    res.append(c)
                    prev = c
                    break
        
        return "".join(res)
