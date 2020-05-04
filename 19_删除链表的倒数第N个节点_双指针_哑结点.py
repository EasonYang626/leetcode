# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 利用哑结点统一 只有一个结点 和 空结点的情况
# 双指针 其中一个先走n + 1步 保证距离为n
# 第一个指针走到空的时候
# 第二个指针指向 要删除的节点前一个节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummynode = ListNode(0)
        dummynode.next = head
        first = dummynode
        second = dummynode
        # 先走n+1步，保证两指针间距离为n
        for i in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummynode.next