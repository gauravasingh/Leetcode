import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        min_heap = []
        result = []

        # Initializing heap with the smallest pair from nums2 for the first min(k, len(nums1)) elements in nums1
        for i in range(min(k, len(nums1))):
            # Each entry: (sum, index in nums1, index in nums2)
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        # Extracting the k smallest pairs
        while min_heap and len(result) < k:
            total, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            # If there's a next element in nums2, push the next pair for the same nums1[i]
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result
