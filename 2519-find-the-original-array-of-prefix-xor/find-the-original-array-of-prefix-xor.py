# class Solution:
#     def findArray(self, pref: List[int]) -> List[int]:
#         n = len(pref)
#         arr = [0] * n
        
#         arr[0] = pref[0]
#         for i in range(1, n):
#             arr[i] = pref[i - 1] ^ pref[i]
        
#         return arr
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        for i in range(len(pref) - 1, 0, -1):
            pref[i] ^= pref[i - 1]
        return pref