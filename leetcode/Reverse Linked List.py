# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode):
        if (not head or not head.next):
          return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead