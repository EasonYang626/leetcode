class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        jinwei = 0
        head = ListNode(0)
        temp = head
        # 注意head的写法
        while l1 or l2:
            # 用xy指定值，不存在则置为0，统一操作，变为0012+1234
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + jinwei
            jinwei = sum//10
            # 先对temp.next赋值，再另temp指向temp.next
            temp.next = ListNode(sum%10)
            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # 两个数最后同时为None，但是进位还为1，如5+5
        if jinwei!=0:
            temp.next = ListNode(1)
        return head.next

