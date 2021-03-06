# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 哈希表
class Solution:
  def hasCycle(self, head):
    seen = set()
    while head:
      if head in seen:
        return True
      seen.add(head)
      head =  head.next
    return False

# 龟兔赛跑算法
class Solution:
  def hasCycle(self, head):
    slow = head
    fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if (slow == fast):
        return True
    return False