from typing  import List
import queue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 思路 用优先队列 k个链表的第一个结点 入队  之后最小的出队
# 出队的结点后面如果还有结点  则继续入队
# 直到队列为空
# 插入删除的复杂度为 log k 
# 一共最多有kn个元素涉及到插入删除的操作
# 时间复杂度为 kn * log k
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        # lists里面可能包含空链表 用None表示
        while  None in lists:
            lists.remove(None)
        if not lists:
            return None

        head = ListNode(0)
        temp = head
        k = len(lists)
        q = queue.PriorityQueue(maxsize = k)
        index = 0        

        for i in range(k):
            # 当元祖的第一个元素相同时 自动比较第二个元素 listnode类型的无法比较
            q.put((lists[i].val, index, lists[i]))
            index = index + 1
            # 用index自增 避免值相同的情况下 比较listnode
            lists[i] = lists[i].next
        while not q.empty():   
            # temp.next 指向从有限队列中出去的 最小结点 也就是元组中的第三个元素  
            temp.next = q.get()[2]
            # 判断从优先队列中出去的 最小的那个结点 后面还有没有结点
            # 有 则继续进入队列
            if temp.next.next:
                q.put((temp.next.next.val, index, temp.next.next))
                index = index + 1
            temp = temp.next
        return head.next

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(4)
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)
c = [a, b]
s = Solution()

print(s.mergeKLists([None]))