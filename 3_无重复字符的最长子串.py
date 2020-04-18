class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        i = 0
        dic = {}
        # 滑动窗口思想，i为窗口左边，j为右边，j-i+1为窗口长度，
        # 也就是窗口内字符串的长度
        # 右侧窗口位置j始终向前滑动
        for j in range(len(s)):
            # 如果找到了相同的字母，则把i滑动到字典中找到的那个字母的位置右侧（如果该位置大于i的话，也就是i不能往回滑动）
            if s[j] in dic:
                i = max(dic[s[j]],i)
            # 字典中以字符串中字母为key，以其位置的右侧一个位置为value
            dic[s[j]] = j+1
            result = max(result,j-i+1)
        return result

      

s = Solution()
print(s.lengthOfLongestSubstring("abba"))
