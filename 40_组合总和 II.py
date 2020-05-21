# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
# 说明：
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 示例 2:
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]


# candidates有重复 且每个数字只能使用一次



from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        length = len(candidates)
        def backtrace(i, tmp_num, tmp):    
            if tmp_num == target:
                # # 去重
                # if tmp not in res:
                res.append(tmp)    
                return        
            if tmp_num > target or i >= length:
                return
            for j in range(i, length):
                if candidates[j] + tmp_num > target:
                    return 
                # 小剪枝 剪去和自己同一高度(i) 的 具有相同结点值的兄弟结点
                if j > i and candidates[j - 1] == candidates[j]:
                    continue
                # 回溯需要跳过当前的数 因为这里一个数只能用一次 
                backtrace(j + 1, tmp_num + candidates[j], tmp + [candidates[j]]) 
            return
        backtrace(0, 0, [])
        return res

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
            


