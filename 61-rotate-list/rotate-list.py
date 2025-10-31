# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 1️ Finding the length of the list and the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        #Computing effective rotations (k may be > length)
        k = k % length
        if k == 0:
            return head

        #Connect the tail to the head to make it circular
        tail.next = head

        # 4 Find the new tail: (length - k - 1)th node
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # 5️ Break the circle and set the new head
        new_head = new_tail.next
        new_tail.next = None

        return new_head
