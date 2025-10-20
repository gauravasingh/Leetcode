# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
       
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            # Identify nodes to swap
            first = current.next
            second = current.next.next

            # Swap
            first.next = second.next
            second.next = first
            current.next = second

            # Move to the next pair
            current = first

        return dummy.next
        