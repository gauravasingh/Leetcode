class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        lcp = []
        for chars in zip(*strs):
            if all(c == chars[0] for c in chars):
                lcp.append(chars[0])
            else:
                break

        return ''.join(lcp)

        