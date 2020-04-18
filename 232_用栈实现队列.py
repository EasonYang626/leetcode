class MyQueue:
    # 思路一：维护两个栈，S1,S2,每次入队时需保证入队元素在栈底才能最后一个出去、
    # 入队前，把S1中所有元素出栈，再依次入栈S2
    # 这样S1中元素顺序就和S2相反，再把入队元素push到S2栈顶
    # 之后再把S2中所有元素出栈，再依次入栈S1
    # 出队，则直接从S1 pop即可
    # 思路二：维护两个栈，Spush（入队栈），Spop（出队栈）
    # 入队则直接push进Spush
    # 出队时，如果Spop为空，则将Spush中所有元素出栈，依次入栈Spop
    # 最后将Spop栈顶元素弹出，
    # 如果Spop非空，则直接弹出Spop栈顶元素
    # 摊还分析：
    # 出队操作最多可以执行的次数跟它之前执行过入队操作的次数有关。
    # 虽然一次出队操作代价可能很大
    # 但是每n次入队才能产生这么一次代价为n的出队操作
    # 因此所有操作的总时间复杂度为：n(所有的入队操作产生） + 2 * n(第一次出队操作产生） + n - 1(剩下的出队操作产生）， 
    # 所以实际时间复杂度为 O(2*n)。于是我们可以得到每次操作的平均时间复杂度为 O(2n/2n)=O(1)
    def __init__(self):

        self.Spush = []
        self.Spop = []

    def push(self, x: int) -> None:

        self.Spush.append(x)

    def pop(self) -> int:

        if len(self.Spop) > 0:
            return self.Spop.pop()
        else:
            self.push2pop()
            return self.Spop.pop()

    def peek(self) -> int:

        if len(self.Spop) > 0:
            return self.Spop[-1]
        else:
            self.push2pop()
            return self.Spop[-1]

    def empty(self) -> bool:

        return (len(self.Spush) == 0 and len(self.Spop) == 0)
    
    def push2pop(self):
        # 把push栈里的元素都放到pop栈中
        while len(self.Spush) > 0:
            self.Spop.append(self.Spush.pop())
mq = MyQueue()
mq.push(5)
print(mq.Spush.pop)
param_2 = mq.pop()
mq.push(6)
param_3 = mq.peek()
param_4 = mq.empty()
print(param_2)
print(param_3)
print(param_4)
