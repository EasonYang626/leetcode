from typing import List
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

# 必须原地修改，只允许使用额外常数空间。

# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 思路：
# 从后向前扫描
# 出现一个数比之前的所有数小的情况
# 则把这个数 和之前的所有数里 比它大的数中 最小的那个 也就是仅大于它的数 交换
# 之后把这个数 后面的所有数 翻转
# 1 5 8 4 7 6 5 3 1
# 找到4 和5 交换
# 1 5 8 5 7 6 4 3 1
# 把7 6 4 3 1逆序翻转
# 1 5 8 5 1 3 4 6 7
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        length = len(nums)
        for i in range(length - 1, 0, -1):
            # 找到第一个小于之前的数的数
            if nums[i - 1] < nums[i]:
                j = i
                # 找到仅大于的数交换
                while j + 1 < length and nums[j + 1] > nums[i - 1]:
                    j += 1
                temp = nums[i - 1]
                nums[i - 1] = nums[j]
                nums[j] = temp
                # 把i - 1之后的逆序翻转
                self.reverse(nums, i)
                return nums
        # 已经没有下一个排列的情况 直接返回最小的排列 升序排列
        return self.reverse(nums, 0)
        # 逆序翻转函数 从start开始翻转 直接对原nums数组原地操作
        # 切片翻转的话 会拷贝一份数组 原数组不变
    def reverse(self, nums, start):
        i = start
        j = len(nums) - 1
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1
        return nums

s = Solution()
a = [1]
s.nextPermutation(a)
print(a)
