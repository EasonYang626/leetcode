from typing import List
class Solution:
    # 排序 + 双指针思路
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if not nums or n < 3:
            return 0
        nums.sort()
        x = abs(nums[0] + nums[1] + nums[2] - target)
        a = 0
        b = 1
        c = 2
        for i in range(n - 2):
            L = i + 1
            R = n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while L < R:
                temp = nums[i] + nums[L] + nums[R] - target
                if temp == 0:
                    return target
                elif temp > 0:
                    if abs(temp) < x:
                        x = abs(temp)
                        a = i
                        b = L
                        c = R
                    R = R - 1
                else:
                    if abs(temp) < x:
                        x = abs(temp)
                        a = i
                        b = L
                        c = R
                    L = L + 1
        return nums[a] + nums[b] + nums[c]

s = Solution()
print(s.threeSumClosest([-10,0,-2,3,-8,1,-10,8,-8,6,-7,0,-7,2,2,-5,-8,1,-4,6] , 18))
