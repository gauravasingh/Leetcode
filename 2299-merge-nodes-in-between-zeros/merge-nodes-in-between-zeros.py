# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        
        current = head.next  # skip first zero
        running_sum = 0
        
        while current:
            if current.val == 0:
                # End of a segment → create new node
                tail.next = ListNode(running_sum)
                tail = tail.next
                running_sum = 0
            else:
                running_sum += current.val
            current = current.next
        
        return dummy.next
