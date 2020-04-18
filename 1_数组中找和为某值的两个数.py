class Solution:
    def twoSum(self,nums,target):
        j = 0
        for i in nums:
            a = nums.index(target - i) if target - i in nums else -1 
            if a == j:
                j = j + 1
                continue
            elif a!=-1:
                list1 = [j,a]
                return list1
            else:
                j = j +1


solution = Solution()
print(solution.twoSum([3,2,4],10))
                