# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases (e.g., removing head)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # prev is the last node before the sublist of duplicates
        curr = head

        while curr:
            # Detect duplicates
            while curr.next and curr.val == curr.next.val:
                curr = curr.next  # skip nodes with the same value

            # If prev.next == curr, no duplicates were detected
            if prev.next == curr:
                prev = prev.next
            else:
                # Skip all duplicates
                prev.next = curr.next

            curr = curr.next

        return dummy.next
