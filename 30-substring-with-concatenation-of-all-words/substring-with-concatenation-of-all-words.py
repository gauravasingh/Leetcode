from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or len(words[0]) == 0:
            return []

        word_len = len(words[0])  # Length of each word
        word_count = Counter(words)  # Frequency count of words
        total_len = word_len * len(words)  # Total length of concatenated words
        result = []

        # Iterate over the first `word_len` characters to cover all possible starting positions
        for i in range(word_len):
            left = i  # Left pointer of the window
            right = i  # Right pointer of the window
            window_word_count = Counter()  # To store the frequency of words in the current window
            words_used = 0  # Number of valid words in the window

            # Slide the window over the string s
            while right + word_len <= len(s):
                # Extract the current word
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    window_word_count[word] += 1
                    words_used += 1

                    # If the word appears more than the required count, move the left pointer
                    while window_word_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window_word_count[left_word] -= 1
                        left += word_len
                        words_used -= 1
                    
                    # If we have exactly the number of valid words, record the starting index
                    if words_used == len(words):
                        result.append(left)
                else:
                    # Reset the window if the word is not in the list
                    window_word_count.clear()
                    words_used = 0
                    left = right

        return result
