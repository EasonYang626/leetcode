# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

# 示例 1:
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 示例 2:
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 思路：
# 动态规划
# 确定状态 转移方程 初始条件 边界情况 计算顺序
# 一种情况 ?()
# 另一种     ?((...))
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        # list用0 初始化所有元素
        dp = [0] * length
        for i in range(1 , length):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                else:
                    pre = i - dp[i - 1] - 1
                    if pre >= 0 and s[pre] == '(':
                        dp[i] = dp[i -1] + 2
                        if pre > 0:
                            dp[i] += dp[pre - 1]
                    
        return max(dp)
s = Solution()
print(s.longestValidParentheses(")()())"))
        