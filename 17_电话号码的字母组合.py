from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':['a','b','c'],
               '3':['d','e','f'], 
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z'] }
        if not digits:
            return []
        res = ['']
        # 这里用到的思想是 当前的状态只和之前的一个状态有关 整体考虑的话 可能就需要输入数字个数的嵌套循环了
        # 这样只需要三层循环
        # 用res记录当前状态 不断更新 从res拿出a 有 ad ae af 拿出b 有bd be bf
        # 最后把ad ar af bd be bf全部更新为res的值
        # 这里用到的是python语法糖 列表推导式 list comprehension
        # 可以写到一行 也可以多行 顺序就是在前的for循环是外层的 在后的是内层的
        # 这里用res的值来更新res 相当于 a = a + 1的道理
        for i in digits:
            res = [pre + suf
                for pre in res
                for suf in dic[i]]
        return res
s = Solution()
print(s.letterCombinations('23'))