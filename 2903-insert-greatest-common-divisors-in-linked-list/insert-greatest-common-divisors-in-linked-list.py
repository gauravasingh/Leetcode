# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr and curr.next:
            g = gcd(curr.val, curr.next.val)       # compute gcd
            new_node = ListNode(g, curr.next)     # create inserted node
            curr.next = new_node                  # link it
            
            curr = new_node.next                  # move two steps forward
        
        return head
