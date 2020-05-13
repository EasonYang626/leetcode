# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 你可以假设数组中不存在重复的元素。
# 你的算法时间复杂度必须是 O(log n) 级别。
# 示例 1:
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
from typing import List
# 思路 数组分一半 一定有一半是有序的 有一半可能有序 或部分有序
# 有序的数组 就能判断目标值在不在其中了 在其中 则对有序二分
# 不在其中 则对剩下的数组继续上述操作
# 用第一个元素和中间元素的大小关系判断是否有序

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        length = len(nums)
        L = 0
        R = length - 1
        while L <= R:
            mid = (L + R)//2
            if nums[mid] == target:
                return mid
            # 这里必须有等于号 处理 L = mid 的情况 让L = mid + 1
            # 放到下面会出现 R = mid - 1 = L -1 丢解的情况
            if nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1      
        return -1
s = Solution()
print(s.search([3, 1], 1))