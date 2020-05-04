class Solution:    
    # 利用python的max()和min()，在Python里字符串是可以比较的
    # 按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。
    # 这里是按位比较 最小的是前面都最小 且最短 
    # 最大的是 前面都最大 且最长
    # 所以最大 和 最小可以看成是差距最大的两个字符串 
    # 可以这样考虑 s1[0] 和 s2[0] 如果一致 则说明其他所有字符串的第一个字符 都是相同的  结果中加入这一部分 —— 说明加入的不多
    # 因为ascii码差距最大的两个数 s1[0] 和 s2[0]都一样了 中间就必须是一样的
    # s1[1] s2[1]如果不一致 则返回之前一致的部分 其他的字符串就算有和s[1]一致的 也没用了 结果中不加入这一部分 —— 说明不加入的不漏
    # 所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1
s = Solution()
print(s.longestCommonPrefix(['abaa','aba','baa','baab']))