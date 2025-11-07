class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]  # Initialize with the first triplet

        for i in range(n - 2):
            # Skipping duplicate first elements for a tiny speed-up
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                # Updating closest if this sum is better
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                # Move pointers intelligently
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    # Found exact match — can't get closer than this
                    return curr_sum

        return closest
