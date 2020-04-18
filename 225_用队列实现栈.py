# 思路一 用两个队列实现，q1，q2，入队时正常入q1
# 这样出队时，就要保证每次出队的为q1队尾元素如[5,4,3,2,1]要出5，队首为1
# 将q1中除最后一个元素外全部出队，再入队到q2 [4,3,2,1]
# 之后将q1最后一个元素出队，即为栈顶元素
# 然后q1 = q2 q2=[]或者通过temp交换q1 q2
# 思路二 用一个队列实现栈
# 入队时 顺序入队 逆序存储
# 如[1,2] 3 入队 [3,1,2]
# 之后队列中仅保存队尾元素，即栈顶元素，全部出队，再依次入队，把队尾变成队首
# 2出队入队[2,3,1]
# 1出队入队[1,2,3]
# 这样就保证了 队首元素即为栈顶元素
# 出队时正常出

class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        L = len(self.queue)
        while L > 1:
            self.queue.append(self.queue.pop(0))
            L = L - 1

    def pop(self) -> int:
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return (len(self.queue) == 0)
ms = MyStack()
ms.push(1)
ms.push(2)
ms.pop()
print(ms.top()) 
