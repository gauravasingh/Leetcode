class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sorting to handle duplicates easily
        res = []

        def backtrack(start, path):
            res.append(path[:])  # Adding the current subset
            for i in range(start, len(nums)):
                # Skipping duplicates at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
