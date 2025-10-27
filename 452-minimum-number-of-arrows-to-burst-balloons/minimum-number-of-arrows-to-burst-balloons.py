class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        # Step 1: Sort balloons by end coordinate
        points.sort(key=lambda x: x[1])
        
        arrows = 1  # At least one arrow for the first balloon
        arrow_pos = points[0][1]
        
        # Step 2: Iterate and decide when to shoot new arrows
        for start, end in points:
            if start > arrow_pos:
                # Need a new arrow since current balloon starts after last arrow
                arrows += 1
                arrow_pos = end  # Shoot new arrow at current balloon's end
        
        return arrows
