class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n

        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only start counting if this is the start of a sequence
            prev = num - 1
            if prev not in num_set:
                curr = num
                streak = 1

                while (curr + 1) in num_set:
                    curr += 1
                    streak += 1

                # Early exit: can’t find longer than remaining numbers
                if streak > n - longest:
                    return streak

                if streak > longest:
                    longest = streak

        return longest
