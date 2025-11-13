class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)

        # Compute prefix XORs
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        ans = 0
        # Iterate over all pairs (i, k)
        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    ans += (k - i)
        return ans
