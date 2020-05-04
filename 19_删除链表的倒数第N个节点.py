# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 要考虑 删除第一个节点的情况
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        temp = head
        i = 0
        dic = {}
        if not head.next:
            return None
        while temp:
            dic[i] = temp
            i = i + 1
            temp = temp.next
        if i == n:
            head = head.next
            return head
        A = dic[i - n - 1]
        B = dic[i - n]
        A.next = B.next
        B.next = None
        return head
# s = Solution()
# print(s.removeNthFromEnd())
