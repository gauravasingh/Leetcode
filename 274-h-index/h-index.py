class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        count = [0] * (n + 1)
        
        # Count citations, capping any value greater than n
        for c in citations:
            count[min(c, n)] += 1
        
        papers = 0
        # Traverse from high to low
        for h in range(n, -1, -1):
            papers += count[h]
            if papers >= h:
                return h
