import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Pairing up (required capital, profit) and sort by required capital
        projects = sorted(zip(capital, profits))
        max_heap = []  # max-heap for available profits (store as negative)
        i = 0  # pointer over sorted projects

        for _ in range(k):
            # Adding all projects that can be started with current capital
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            # No available projects? Stop early
            if not max_heap:
                break

            # Selecting the project with the highest profit
            w -= heapq.heappop(max_heap)  # subtract because profits are stored as negatives

        return w
