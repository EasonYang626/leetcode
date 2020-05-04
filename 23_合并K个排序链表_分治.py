from typing  import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 分治思想
# 合并K个链表 看成合并两个链表 一个是合并前k/2个链表的结果 一个是合并后k/2个链表的结果
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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)
        # 定义递归出口
        if length == 0:
            return None
        if length == 1:
            return lists[0]
        mid = length // 2
        # mergeKlists函数合并多个链表 返回一个链表
        # mergeTwoLists函数合并两个链表 返回一个链表
        # 所以这里可以直接返回 合并两个列表的结果
        # 参数是 合并前一半的链表的返回值 和 合并后一半链表的返回值
        return self.mergeTwoLists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:length])) 