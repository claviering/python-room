# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        l1Head = l1
        l2Head = l2
        carry = 0 # 进位
        while l1 and l2:
            tmpSum = l1.val + l2.val + carry
            carry = tmpSum // 10
            l1.val = tmpSum % 10
            l2.val = tmpSum % 10
            if not l1.next and not l2.next and carry:
                l1.next = ListNode(1)
                carry = 0
            l1 = l1.next
            l2 = l2.next
        if (l1):
            while carry > 0:
                tmpSum = l1.val + carry
                l1.val = tmpSum % 10
                carry = tmpSum // 10
                if (not l1.next and carry > 0):
                    l1.next = ListNode(1)
                    break
                l1 = l1.next
            return l1Head
        elif l2:
            while carry > 0:
                tmpSum = l2.val + carry
                l2.val = tmpSum % 10
                carry = tmpSum // 10
                if (not l2.next and carry > 0):
                    l2.next = ListNode(1)
                    break
                l2 = l2.next
            return l2Head
        else:
            return l1Head

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
def test5():
    a = ListNode(1)
    b = ListNode(9, ListNode(9, ListNode(9)))
    sol = Solution()
    s = sol.addTwoNumbers(a, b)
    while s:
        print(s.val)
        s = s.next
def test6():
    a = ListNode(0, ListNode(8, ListNode(6)))
    b = ListNode(6, ListNode(7, ListNode(8)))
    sol = Solution()
    s = sol.addTwoNumbers(a, b)
    while s:
        print(s.val)
        s = s.next

# print('test1')
# test1()
# print('test2')
# test2()
# print('test3')
# test3()
# print('test4')
# test4()
# print('test5')
# test5()
print('test6')
test6()