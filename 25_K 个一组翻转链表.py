# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 思路还是递归 多加一个单独的函数 输入参数为链表头 以及链表内的结点数
# 返回为翻转后的链表的头
# 
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:        
        cur = head
        index = k
        # 如果结点数大于等于k个 cur指向第k个结点
        while cur and index > 1:
            cur = cur.next
            index = index - 1
        # 对链表中的结点数小于k的情况 则不需要进行处理
        if not cur:
            return head
        # 翻转前k个结点
        # pre代表cur在翻转后应该指向的结点
        # 把第k + 1个结点传入函数 返回值应该是翻转好后的链表的头结点
        pre = self.reverseKGroup(cur.next, k)
        cur = head
        index = k
        # 执行k次循环
        # 每次temp保存为当前结点的下一个结点
        # 之后让当前结点指向pre结点
        # 然后pre结点更新为当前结点
        # 当前结点更新为temp
        # 每次循环完成一个当前结点的指向修改任务
        # 之后把它保存为pre
        while cur and index > 0:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp 
            index = index - 1      
        return pre
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
s = Solution()
s.reverseKGroup(a, 2)

