from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Step 1: Compute the maximum possible OR
        target_or = 0
        for num in nums:
            target_or |= num

        self.count = 0
        n = len(nums)

        # Step 2: DFS to count subsets whose OR equals target_or
        def dfs(index: int, current_or: int):
            if index == n:
                if current_or == target_or:
                    self.count += 1
                return

            # Include nums[index]
            dfs(index + 1, current_or | nums[index])

            # Exclude nums[index]
            dfs(index + 1, current_or)

        dfs(0, 0)
        return self.count
