class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for xj, yj, rj in queries:
            r2 = rj * rj
            count = 0
            for xi, yi in points:
                if (xi - xj)**2 + (yi - yj)**2 <= r2:
                    count += 1
            res.append(count)
        return res
