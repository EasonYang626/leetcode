# 给定一个非负整数数组，你最初位于数组的第一个位置。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。

# 示例:

# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 说明:

# 假设你总是可以到达数组的最后一个位置。
from typing import List



class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length
        if length == 1:
            return 0
        # 代表从当前位置到最后的最小步数
        for i in range(length):
            index = length - i - 1

            # 直接就能跳过去
            if nums[index] >= i:
                dp[index] = 1
            else:
                dp[index] = dp[index + 1] + 1
                for j in range(2, nums[index] + 1):
                    if dp[index + j] +  1 < dp[index]:
                        dp[index] = dp[index + j] +  1
        return dp[0]
# 贪心法
class Solution2:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            # 当前 i 点最多走多远
            maxPos = max(maxPos, i + nums[i])
            # i等于end 时 说明把当前的能够到达的点都考虑完了
            if i == end:
                end = maxPos
                step += 1
            # 可以到达终点了 直接返回
            if end > n - 2:
                return step
        return step




s = Solution2()
print(s.jump([2,3,1,2,4,2,3]))

