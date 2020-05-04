from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 解题思路：双指针
        # 维护两个指针 分别指向容器的左右边缘 L R 
        # L 只能向右移动 R 只能向左移动
        # 则最大盛水容量为 min(height(L),height(R)) * (R-L)
        # 如果height(L)是较小的那一个 则将L向右移动
        # 因为此时 无论向左移动多少R 都不可能得到一个比之前的结果更大的
        # 假设左移之后 height(R)大于height(L) 那么min结果还是height(L) 且R-L变小了
        # 假设左移之后 height(R)小于height(L) 那么min结果是更小的height(R) 且R-L还变小了
        # 都会导致乘积结果更小
        L = 0
        R = len(height) - 1
        res = 0
        while L != R:
            res = max(res,min(height[L],height[R]) * (R - L))
            if height[L] <= height[R]:
                L = L + 1
            else:
                R = R - 1
        return res
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
