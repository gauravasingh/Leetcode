class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # stores last seen index of each character
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            # If the character is already in the window, move the left pointer
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            
            char_index[char] = right  # update last seen position
            max_len = max(max_len, right - left + 1)
        
        return max_len
