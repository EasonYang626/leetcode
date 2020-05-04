from typing import List
# 排序 + 双指针 思路
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        if(not nums or n < 3):
            return []
        nums.sort()
        for i in range(n - 2):
            # 如果i对应的数大于零 则直接返回 
            # 因为后面的数都大于零了 不可能出现和为0的情况了
            if nums[i] > 0:
                return res
            # 在开始后面的判断前 先判断当前位置的数和前一个位置的数是否一致
            # 一致则直接跳过 否则会重复
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = n - 1
            # L指针指向i右边一个数  R指向结尾
            while L < R:
                # 三个数和为零则加入结果中，并作排除之后重复的判断
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i] , nums[L] , nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L = L + 1
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1   
                    # 注意这里！！结束之后需要同时将L指针右移 R指针左移 
                    # 因为如果只右移L 则会大于0 之后还需要左移R 重复操作会增加
                    L = L + 1
                    R = R - 1            
                #这里如果和小于零 则左边数需要增加   
                elif nums[i] + nums[L] + nums[R] < 0:
                    L = L + 1
                #否则右边数需要减小
                else :
                    R = R - 1
        return res

s = Solution()
print(s.threeSum([0,0,0]))



