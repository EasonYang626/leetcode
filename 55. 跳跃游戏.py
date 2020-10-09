from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1:
            return True
        for i in range(2, length + 1):
            if nums[length - i] >= i - 1:
                return self.canJump(nums[0:length - i + 1])
        return False


# 循环替换递归
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1:
            return True
        while length > 1:
            for i in range(2, length + 1):
                if nums[length - i] >= i - 1:
                    nums = nums[0:length - i + 1]
                    length = length - i + 1
                    break
                if i == length:
                    return False
        return True


class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        # n代表需要跳多远
        n = 1
        # 注意for 包前不包后
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= n:
                n = 1
            else:
                # 当前能跳的距离无法满足到达最后，则需要跳的长度+1
                n += 1
            if i == 0 and n > 1:
                return False
        return True


s = Solution2()
print(s.canJump([2, 3, 1, 1, 4]))
