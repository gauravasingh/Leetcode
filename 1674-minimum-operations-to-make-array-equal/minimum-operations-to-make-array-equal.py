class Solution:
    def minOperations(self, n: int) -> int:
        # n is even
        if n % 2 == 0:
            k = n // 2
            return k * k
        # n is odd
        else:
            k = n // 2
            return k * (k + 1)
