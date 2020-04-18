class Solution:
    def twoSum(self,nums,target):
        dic = {}
        # enumerate(iterable[, start]) -> iterator for index, value of iterable
        for i,num in enumerate(nums):
            if target - num in dic :
                return [dic[target - num],i]
            dic[num] = i
            # 字典中以数组中元素为key以出现位置为value

solution = Solution()
print(solution.twoSum([3,2,4],6))