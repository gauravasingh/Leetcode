class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        ans = [0] * m
        
        for i in range(m):
            r, c = startPos
            count = 0
            
            for j in range(i, m):
                move = s[j]
                if move == 'L':
                    c -= 1
                elif move == 'R':
                    c += 1
                elif move == 'U':
                    r -= 1
                else:  # 'D'
                    r += 1
                
                # If out of bounds, stop
                if not (0 <= r < n and 0 <= c < n):
                    break
                
                count += 1
            
            ans[i] = count
        
        return ans
