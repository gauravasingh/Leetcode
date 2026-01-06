class Solution:
    def maxDistinct(self, s: str) -> int:
        # set to count all distinct characters
        return len(set(s))

# Example 
sol = Solution()
print(sol.maxDistinct("abab"))  # Output: 2
print(sol.maxDistinct("abcd"))  # Output: 4
print(sol.maxDistinct("aaaa"))  # Output: 1
