# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Helper: reverse [start, end)
        def reverse(start, end):
            prev = end
            curr = start
            while curr != end:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev  # new head of the reversed sublist

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # Find the kth node
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # less than k nodes remain

            group_next = kth.next  # node after kth

            # Reverse the k-group
            new_group_head = reverse(group_prev.next, group_next)

            # Reconnect reversed part
            temp = group_prev.next
            group_prev.next = new_group_head
            group_prev = temp  # move to the next group
