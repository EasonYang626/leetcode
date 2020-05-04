# 递归思路
# 1 函数是干什么的 想明白功能
# 2 递归出口
# 3 找出函数的等价关系式
from typing import List

# 用栈 遍历状态树 避免了递归
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # (parentheses, #left, #right)
        # n n 代表剩余的左括号 和 右括号的数目
        # stack存储 状态树包含当前字符串 和剩余的括号数目
        stack = [('',n,n)]
        ans = []
        while stack:
            # 弹出当前状态
            #    左右括号都不剩了 把当前字符串加入结果中
            p,left,right = stack.pop()
            if left == right == 0:
                ans.append(p)
                continue     
            # 如果左括号还有剩余 则当前字符串右边加一个左括号 
            # 再压入栈中
            # 下面的两个判断 和压栈 都是针对于当前状态的
            # 每次把当前状态的两种情况考虑清楚 如果可以 就压栈
            # 下一次对栈顶 也就是最近压入的合法状态 再进行判断
            # 直到左右都不剩了 才只弹出 不压入 之后继续判断下一个栈顶 状态
            if left > 0:
                stack.append((p + '(',left - 1,right))
            # 如果右括号还有剩的 且右括号剩的比左括号多 则当前字符串右边加一个右括号
            # 这样就保证了字符串是合法的
            if right > 0 and right > left:
                stack.append((p + ')',left,right - 1))
        return ans
s = Solution()
s.generateParenthesis(2)        
        

