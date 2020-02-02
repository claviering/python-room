# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if (not head or not head.next):
          return head
        self.swapPairs(head.next.next)
        head.next.val, head.val = head.val, head.next.val
        return head