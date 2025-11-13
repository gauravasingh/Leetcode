class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        #  Base pickup time (1 min per piece)
        total_time = sum(len(g) for g in garbage)

        # Compute prefix sum of travel times
        prefix = [0] * (len(travel) + 1)
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] + travel[i - 1]

        #  Find last house for each type
        last = {'M': 0, 'P': 0, 'G': 0}
        for i in range(len(garbage)):
            for c in garbage[i]:
                last[c] = i

        #  Add travel time for each truck
        for c in "MPG":
            total_time += prefix[last[c]]

        return total_time
