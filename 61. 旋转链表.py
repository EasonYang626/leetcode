# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        temp = head
        length = 0
        # 计算链表的长度
        while temp:
            temp = temp.next
            length += 1
        k = k % length
        # 找到开头节点前一个结点
        temp = head
        for i in range(length - k - 1):
            temp = temp.next
        res = temp.next
        # 只有一个结点的情况
        if not res:
            return head
        # 赋给res开头节点之后，令开头节点的前一个结点指向空
        temp.next = None
        temp = res
        while temp.next:
            temp = temp.next
        # 找到最后一个结点，指向头结点
        temp.next = head
        return res
