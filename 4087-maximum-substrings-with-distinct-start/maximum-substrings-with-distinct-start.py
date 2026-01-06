class Solution:
    def maxDistinct(self, s: str) -> int:
        # Use a set to count all distinct characters
        return len(set(s))

# Example usage:
sol = Solution()
print(sol.maxDistinct("abab"))  # Output: 2
print(sol.maxDistinct("abcd"))  # Output: 4
print(sol.maxDistinct("aaaa"))  # Output: 1
