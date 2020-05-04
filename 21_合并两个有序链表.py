# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        temp = head
        while l1 or l2:
            if not l1:
                temp.next = l2
                break
            if not l2:
                temp.next = l1
                break
            if l1.val > l2.val:
                # temp.next = ListNode(l2.val)
                temp.next = l2
                temp = temp.next
                l2 = l2.next
            else:
                # temp.next = ListNode(l1.val)
                temp.next = l1
                temp = temp.next
                l1 = l1.next
        return head.next
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(4)
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)
s = Solution()
print(s.mergeTwoLists(a,b))
