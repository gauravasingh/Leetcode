class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def backtrack(curr):
            if len(curr) == n:
                res.append(curr)
                return
            # You can always add '1'
            backtrack(curr + '1')
            # You can add '0' only if the previous character isn't '0'
            if not curr or curr[-1] != '0':
                backtrack(curr + '0')

        backtrack("")
        return res
