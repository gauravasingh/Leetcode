# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize matrix with -1
        matrix = [[-1] * n for _ in range(m)]

        top, bottom = 0, m - 1
        left, right = 0, n - 1

        curr = head

        while curr and top <= bottom and left <= right:
            # Traverse left → right
            for col in range(left, right + 1):
                if not curr: break
                matrix[top][col] = curr.val
                curr = curr.next
            top += 1

            # Traverse top → bottom
            for row in range(top, bottom + 1):
                if not curr: break
                matrix[row][right] = curr.val
                curr = curr.next
            right -= 1

            if top <= bottom:
                # Traverse right → left
                for col in range(right, left - 1, -1):
                    if not curr: break
                    matrix[bottom][col] = curr.val
                    curr = curr.next
                bottom -= 1

            if left <= right:
                # Traverse bottom → top
                for row in range(bottom, top - 1, -1):
                    if not curr: break
                    matrix[row][left] = curr.val
                    curr = curr.next
                left += 1

        return matrix
