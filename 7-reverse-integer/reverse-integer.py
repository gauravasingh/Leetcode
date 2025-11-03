class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        sign = -1 if x < 0 else 1
        x *= sign  # make x positive for easier manipulation
        
        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check overflow before multiplying by 10
            if rev > (INT_MAX - digit) // 10:
                return 0  # overflow
            
            rev = rev * 10 + digit
        
        return sign * rev
