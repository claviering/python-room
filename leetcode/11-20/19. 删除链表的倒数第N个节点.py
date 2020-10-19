# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 方法一：计算链表长度
class Solution:
  def removeNthFromEnd(self, head, n):
    length = 0
    point = head
    while point:
      length = length + 1
      point = point.next
    # 只有一个节点
    if length == 1 and n == 1:
      return None
    # 删除第一个节点
    if length == n:
      return head.next
    point = head
    step = 0
    deleteIndex = length - n - 1
    while step < deleteIndex:
      step = step + 1
      point = point.next
    point.next = point.next.next
    return head

# 方法三：一次遍历 双指针
# 两个指针 first 和 second 同时对链表进行遍历, 相隔 n + 1 步，同时先前遍历 
# 当 first 为 None 的时候, second.next = second.next.next
class Solution:
  def removeNthFromEnd(self, head, n):
    first = head
    second = head
    first_step = 0 # 记录 first 走的步数
    while first_step < n:
      first = first.next
      first_step = first_step + 1
    if first == None:
      return second.next
    while first.next:
      first = first.next
      second = second.next
    second.next = second.next.next
    return head