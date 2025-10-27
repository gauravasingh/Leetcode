from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Dictionary to hold sorted string as key and list of anagrams as value
        anagrams = defaultdict(list)
        
        for s in strs:
            # Sort the characters in the string -> tuple used as dict key (hashable)
            key = tuple(sorted(s))
            anagrams[key].append(s)
        
        # Return grouped anagrams as a list of lists
        return list(anagrams.values())
