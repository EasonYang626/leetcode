
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个字符串完全匹配才算匹配成功。

# 说明:

# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。




class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 递归 递归式 + 递归出口 递归处理好当前 不管后面
        if not p:    #p为空 且 s 为空 则返回true
            return not s
        if not s:
            if not p:
                return True
            if set(p) == {'*'}:
                return True
            return False
        if p[0] == '?' or p[0] == s[0]:
            return self.isMatch(s[1:], p[1:])
        if p[0] == '*':
            return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
        return False

# 思路
# 双指针 回溯法
# 优先看是不是一对一匹配 直接跳 i j
# 之后看j 对应的是不是* 是直接跳 * 这里先考虑* 匹配零个字符的情况
# 之后继续 如果不匹配了 回溯 j 回到* 之后 i 回到之前的后一个位置 表示用*匹配了一个字符
# 再继续 不匹配 就用*匹配两个字符
class Solution2:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        start = -1
        match = 0
        while i < len(s):
            # 一对一匹配,匹配成功一起移
            if j < len(p) and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            # 记录p的"*"的位置,还有s的位置
            elif j < len(p) and p[j] == "*":
                start = j
                match = i
                # 这里没有用*匹配任何字符
                j += 1
            # j 回到 记录的下一个位置
            # match 更新下一个位置
            # 这代表用*匹配一个字符
            elif start != -1:
                j = start + 1
                match += 1
                i = match
            else:
                return False
         # 将多余的 * 直接匹配空串
        return all(x == "*" for x in p[j:])        


s = Solution2()
print(s.isMatch("acdcb","a*cb"))