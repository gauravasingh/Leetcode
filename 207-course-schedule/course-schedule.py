from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:  # found a cycle
                return False
            if state[course] == 2:  # already processed safely
                return True

            state[course] = 1  # mark as visiting
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            state[course] = 2  # mark as done
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
