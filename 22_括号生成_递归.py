# 递归思路
# 1 函数是干什么的 想明白功能
# 2 递归出口
# 3 找出函数的等价关系式
from typing import List
# 用一个新函数递归 方便传参
class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def func(string, L, R):
            if L == 0 and R == 0:
                res.append(string)   
                return
            if L > 0:
                func(string + '(', L - 1, R)
            if R > L:
                func(string + ')', L, R - 1)
        func('', n, n)
        return res

s = Solution()
print(s.generateParenthesis(3))