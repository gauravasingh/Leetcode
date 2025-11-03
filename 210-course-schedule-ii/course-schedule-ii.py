from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
        order = []
        self.valid = True

        def dfs(course):
            if not self.valid:
                return
            visited[course] = 1
            for neighbor in graph[course]:
                if visited[neighbor] == 0:
                    dfs(neighbor)
                elif visited[neighbor] == 1:
                    self.valid = False  # cycle found
            visited[course] = 2
            order.append(course)

        for c in range(numCourses):
            if visited[c] == 0:
                dfs(c)

        return order[::-1] if self.valid else []
