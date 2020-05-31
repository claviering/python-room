# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        head = ListNode()
        tail = head
        next = 0 # 进位
        while l1 or l2:
            tmpNode = ListNode()
            tmpSum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + next
            tmpNode.val = tmpSum % 10
            next = tmpSum // 10
            tail.next = tmpNode
            tail = tail.next
            if (l1):
                l1 = l1.next
            if (l2):
                l2 = l2.next
        if (next):
            tmpNode = ListNode()
            tmpNode.val = next
            tail.next = tmpNode
            tail = tail.next
        return head.next

def test1():
    a = ListNode(2, ListNode(4, ListNode(3)))
    b = ListNode(5, ListNode(6, ListNode(4)))
    sol = Solution()
    s = sol.addTwoNumbers(a, b)
    while s:
        print(s.val)
        s = s.next
def test2():
    a = ListNode(5)
    b = ListNode(5)
    sol = Solution()
    s = sol.addTwoNumbers(a, b)
    while s:
        print(s.val)
        s = s.next

def test3():
    a = ListNode(2)
    b = ListNode(5, ListNode(6, ListNode(4)))
    sol = Solution()
    s = sol.addTwoNumbers(a, b)
    while s:
        print(s.val)
        s = s.next

def test4():
    a = ListNode(2, ListNode(4, ListNode(3)))
    b = ListNode(5)
    sol = Solution()
    s = sol.addTwoNumbers(a, b)
    while s:
        print(s.val)
        s = s.next

print('test1')
test1()
print('test2')
test2()
print('test3')
test3()
print('test4')
test4()