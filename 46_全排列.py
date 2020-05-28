# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。

# 示例:

# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
from typing import List
import copy

class Solution:   
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrace(num, res):            
            if res == []:
                res.append([num])
                return
            temp_res = [] 
            while res != []:
                sub_res = res.pop()
                length = len(sub_res)                             
                for i in range(length + 1):
                    temp = sub_res.copy()
                    temp.insert(i, num)                   
                    temp_res.append(temp)
            for i in temp_res:
                res.append(i)
            # res = copy.deepcopy(temp_res)
           
        for i in nums:
            backtrace(i, res)
        return res

s = Solution()
print(s.permute([0,1]))