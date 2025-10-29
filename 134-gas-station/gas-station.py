class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_tank = 0
        current_tank = 0
        start = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]
            
            # If we run out of gas, next station becomes start
            if current_tank < 0:
                start = i + 1
                current_tank = 0
        
        return start if total_tank >= 0 else -1
