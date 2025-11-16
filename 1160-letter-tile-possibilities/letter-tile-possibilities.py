class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
        
        count = Counter(tiles)
        
        def dfs(counter):
            total = 0
            for letter in counter:
                if counter[letter] > 0:
                    total += 1  # choosing this letter creates a new sequence
                    counter[letter] -= 1
                    total += dfs(counter)
                    counter[letter] += 1
            return total
        
        return dfs(count)
