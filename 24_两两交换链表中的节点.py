# Definition for singly-linked list.
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# .next可以翻译为指向的
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        # 对链表里没有节结点 和一个结点处理后 剩下两个结点以上的情况
        # dummyhead指向的赋值为head指向的 也就是dummyhead指向第二结点
        # 第二结点也就是要返回的链表的头结点
        dummyhead = ListNode(0)
        dummyhead.next = head.next     
        # temp赋值为第二结点   
        temp = head.next
        # 第一结点指向的 赋值为 把第三结点当成参数 传入函数的 返回值
        # 返回值就是已经调换好顺序的链表的头结点
        head.next = self.swapPairs(temp.next)
        # 第二结点指向的 赋值为 第一结点
        temp.next = head
        return dummyhead.next

    
