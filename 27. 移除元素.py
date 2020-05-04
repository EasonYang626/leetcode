from typing import List
# i是慢指针 j是快指针
# 双指针赋值 j一直向前走
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        if not List:
            return 0
        for j in range(0, len(nums)):
            if nums[j]!= val:
                nums[i] = nums[j]
                i = i + 1
        return i
# 当i对应的元素和val一样时 把最后一个元素的值赋值到i对应的元素
# i不变 下次循环还会检查这个元素 防止最后一个元素还是val 之后长度减一 
class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n = n - 1
            else:
                i = i + 1
        return n


