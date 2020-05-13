# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:
# 输入: [1,3,5,6], 2
# 输出: 1
# 示例 3:
# 输入: [1,3,5,6], 7
# 输出: 4
# 示例 4:
# 输入: [1,3,5,6], 0
# 输出: 0
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return None
        length = len(nums)
        L = 0
        R = length - 1
        while L <= R:
            mid = (L + R)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1
        return L
s = Solution()
print(s.searchInsert([1,3,5,6], 0))