from typing import List

# 该算法更为简便之处是忽略了对子序列的寻找比较,而是根据规律直接找出最佳答案.
# 对于含有正数的序列而言,最大子序列肯定是正数,所以头尾肯定都是正数
# 我们可以从第一个正数开始算起,每往后加一个数便更新一次和的最大值;当当前和成为负数时,
# 则表明此前序列无法为后面提供最大子序列和,因此必须重新确定序列首项.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        sum = 0
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            res = max(res, sum)
        return res

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
