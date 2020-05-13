# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 你的算法时间复杂度必须是 O(log n) 级别。
# 如果数组中不存在目标值，返回 [-1, -1]。
# 示例 1:
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
# 思路 两次二分搜索
# 第一次找左边界 从右侧逼近 收紧
# 第二次找右边界 从左侧逼近 收紧
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        length = len(nums)
        L = 0
        R = length - 1
        start = -1
        end = -1
        # 左边界 右侧收紧
        while L <= R:
            mid = (L + R)//2
            if nums[mid] == target:
                R = mid - 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1
        # 该函数返回的是 有L个元素小于target
        # 如果全部元素小于target的情况
        if L >= length or nums[L] != target :
            start = -1
        else:
            start = L
        # 左边界没有 则直接返回没找到的结果
        if start == -1:
            return [-1, -1]
        # 重新初始化
        L = 0
        R = length - 1            
        # 找右边界 左侧收紧
        while L <= R:
            mid = (L + R)//2
            if nums[mid] == target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1    
        # 如果全部元素都大于target的情况 R = -1
        if R < 0 or nums[R] != target :
            end = -1
        else:
            end = R
        return [start, end]
        
s = Solution()
print(s.searchRange([1], 2))