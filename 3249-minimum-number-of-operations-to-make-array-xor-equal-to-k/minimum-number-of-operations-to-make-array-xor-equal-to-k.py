class Solution:
    def minOperations(self, nums, k):
        from functools import reduce
        from operator import xor
        
        X = reduce(xor, nums, 0)
        
        if X == k:
            return 0
        
        T = X ^ k
        return T.bit_count()
