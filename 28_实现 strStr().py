# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 可以滑动窗口 字符串切片直接比较
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        length = len(needle)
        # 简单回溯 考虑needle串本身 回溯到和第一个字符一样的第二个字符的位置
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i: i + length] == needle:
                    return i
        return -1

s = Solution()
print(s.strStr("mississippi", "issip"))

