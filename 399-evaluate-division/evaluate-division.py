from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Build the graph
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1.0 / val

        # DFS helper to find a path from start → end
        def dfs(curr, target, visited):
            if curr not in graph or target not in graph:
                return -1.0
            if curr == target:
                return 1.0
            visited.add(curr)
            for neighbor, value in graph[curr].items():
                if neighbor in visited:
                    continue
                res = dfs(neighbor, target, visited)
                if res != -1.0:
                    return res * value
            return -1.0

        # Evaluate each query
        result = []
        for a, b in queries:
            result.append(dfs(a, b, set()))
        return result
