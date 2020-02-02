# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
      start = end = ListNode(0)
      while l1 and l2:
        if l1.val < l2.val:
          end.next = ListNode(l1.val)
          l1 = l1.next
        else:
          end.next = ListNode(l2.val)
          l2 = l2.next
        end = end.next
      # 添加剩余节点
      if l1:
        end.next = l1
      if l2:
        end.next = l2
      return start.next