from typing import List

# 示例:
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 思路：
# 双指针
# 左边矮 left指针就从左往右
# 右边矮 right指针就从右往左
# 每次加上 当前的边最高的减去当前高度的差
# 右边高于左边 则右边总会被挡住
# 左边能存多少水 就取决于左边最高的
# 最高的 减去当前高度的水 总能存进去
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        length = len(height)
        right = length - 1
        L_max = 0
        R_max = 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= L_max:
                    L_max = height[left]
                else:
                    res += L_max - height[left]
                left += 1
            else:
                if height[right] >= R_max:
                    R_max = height[right]
                else:
                    res += R_max - height[right]    
                right -= 1                        
        return res
s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))                

