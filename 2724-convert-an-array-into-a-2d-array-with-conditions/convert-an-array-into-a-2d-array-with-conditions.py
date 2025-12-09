class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter

        freq = Counter(nums)
        max_rows = max(freq.values())

        #  empty rows
        result = [[] for _ in range(max_rows)]

        # Distribute each no in diff rows
        for num, count in freq.items():
            for i in range(count):
                result[i].append(num)

        return result

