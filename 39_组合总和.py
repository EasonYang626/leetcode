# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。
# 说明：
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2:
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

# 剪枝提速
# 如果一个数位搜索起点都不能搜索到结果，
# 那么比它还大的数肯定搜索不到结果，
# 基于这个想法，我们可以对输入数组进行排序，以减少搜索的分支；
from typing import List

class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:       
        array = {}
        def backtrace(candidates, target):              
            res = []
            if target < 1 or not candidates:
                return []
            # 有 就直接加进结果中
            if target in candidates:
                res.append([target])            
            for i in candidates:
                # 递归找 target - i 的结果 小于等于0直接跳过
                if target - i < 1:
                    continue
                if target - i not in array:
                    temp = backtrace(candidates, target - i)
                    array[target - i] = temp
                else:
                    temp = array[target - i]                
                # 找到之后加到 i 之后 放到结果中
                if temp != []:
                    for j in temp:
                        subres = []
                        subres.append(i)
                        subres.extend(j)
                        res.append(subres)
            # 排序去重
            new_res = []
            for i in res:               
                if temp not in new_res:
                    new_res.append(temp)
            return new_res
        return backtrace(candidates, target)



# dfs
# s.combinationSum([1, 2],3)
# 选个1 之后再选 只要和不大于target 
# 1 1 1 可以 回溯
# 1 1 2不行
# 1 2 可以 再回溯
# 选2之后没得选了 只能选它本身以及后面的

class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        # backtrack不返回任何值 只是递归中对res的值进行修改
        def backtrack(i, tmp_sum, tmp):
            # 总和已经大于target 则没有解的可能了
            if  tmp_sum > target or i == n:
                return 
            if tmp_sum == target:
                res.append(tmp)
                return 
            # 从第 i 个开始选
            for j in range(i, n):
                # 如果和超了 直接跳出 因为后面的也会超 已经做好排序了
                if tmp_sum + candidates[j] > target:
                    break
                # 没超 就选 再从第j个开始选
                backtrack(j,tmp_sum + candidates[j],tmp+[candidates[j]])
        backtrack(0, 0, [])
        return res
        


s = Solution2()
print(s.combinationSum([1, 2],3))