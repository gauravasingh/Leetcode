class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string into words, automatically trims spaces
        words = s.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join with a single space
        return ' '.join(reversed_words)
