from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def backtrack(start: int, path: List[str]):
            # If we have 4 parts and used all digits
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return
            
            # Trying segments of length 1–3
            for length in range(1, 4):
                if start + length > len(s):
                    break
                
                segment = s[start:start + length]
                
                # Skipping invalid segments (leading zeros or > 255)
                if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                    continue
                
                backtrack(start + length, path + [segment])
        
        backtrack(0, [])
        return res
