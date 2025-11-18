class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s, target, idx, curr_sum):
            # If we reached the end, check if sum == target
            if idx == len(s):
                return curr_sum == target
            
            # Try all possible substrings starting at idx
            for end in range(idx + 1, len(s) + 1):
                val = int(s[idx:end])
                if curr_sum + val > target:
                    break  # no need to continue
                
                if can_partition(s, target, end, curr_sum + val):
                    return True
            
            return False
        
        total = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition(square_str, i, 0, 0):
                total += i * i
        
        return total
