from collections import Counter, defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        t_count = Counter(t)
        window_count = defaultdict(int)

        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_count[char] += 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            # Try to shrink the window when we have all needed characters
            while have == need:
                # Update result if this window is smaller
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Shrink from the left
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
