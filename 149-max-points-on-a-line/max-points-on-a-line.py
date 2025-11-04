from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        max_points = 1
        
        for i in range(len(points)):
            slopes = defaultdict(int)
            duplicates = 0
            cur_max = 0

            x1, y1 = points[i]
            
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                # Normalizing slope by gcd
                g = gcd(dx, dy)
                if g != 0:
                    dx //= g
                    dy //= g

                # Ensuring consistency in slope representation
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slopes[(dx, dy)] += 1
                cur_max = max(cur_max, slopes[(dx, dy)])
            
            max_points = max(max_points, cur_max + duplicates + 1)
        
        return max_points
