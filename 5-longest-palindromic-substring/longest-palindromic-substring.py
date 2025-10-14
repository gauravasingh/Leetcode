class Solution:
    def longestPalindrome(self,s: str) -> str:
    
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
        
            return s[left + 1:right]

        if not s:
            return ""

        longest = ""
        for i in range(len(s)):
            palindrome1 = expandAroundCenter(i, i)
            palindrome2 = expandAroundCenter(i, i + 1)

            longest = max(longest, palindrome1, palindrome2, key=len)

        return longest
    