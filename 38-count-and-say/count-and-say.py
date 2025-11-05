class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        # Starting from 1 and build up to n
        result = "1"
        
        for _ in range(2, n + 1):
            prev = result
            result = ""
            count = 1
            
            # Looping through previous term to build the next
            for i in range(1, len(prev)):
                if prev[i] == prev[i - 1]:
                    count += 1
                else:
                    result += str(count) + prev[i - 1]
                    count = 1
            
            # Last run
            result += str(count) + prev[-1]
        
        return result
