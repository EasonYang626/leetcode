# 双指针
# j一致向前走
# 找到第一个不等于i指向的数
# 就把值赋给i后面的数
# i向前走一步 指向赋值后的数
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        i = 0
        for j in range(1, length):
            # 找到第一个不等于nums[i]的数
            # 之后i = i + 1 i向前走一步
            # 把这个数赋值给nums[i]
            # j继续向前走
            if nums[i] < nums[j]:
                i = i + 1
                nums[i] = nums[j]
        return i + 1


                