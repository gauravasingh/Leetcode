# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head
        
        # Step 1: Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move `prev` to the node just before the sublist to reverse
        for _ in range(left - 1):
            prev = prev.next
        
        # Step 2: Reverse the sublist
        curr = prev.next
        next_node = None
        
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next
