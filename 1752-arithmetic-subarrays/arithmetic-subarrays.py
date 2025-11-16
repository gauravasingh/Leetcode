class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:

        ans = []
        
        for left, right in zip(l, r):
            sub = nums[left:right+1]
            sub.sort()

            diff = sub[1] - sub[0]
            ok = True
            for i in range(1, len(sub)):
                if sub[i] - sub[i-1] != diff:
                    ok = False
                    break

            ans.append(ok)

        return ans

