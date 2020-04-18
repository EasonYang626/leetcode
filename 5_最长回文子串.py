class Solution:
    def longestPalindrome(self, s: str) -> str:
        s1 = "#"
        j = 0
        length = 0
        res = ""
        # 把奇数偶数字符串都变成奇数的
        for i in range(len(s)):
            s1 = s1 + s[i] +"#"
        # 对n个中心依次求解，保存最长的对应的中心和一半的长度
        for i in range(len(s1)):
            temp = self.central(s1,i)
            if temp > length:
                j = i
                length = temp
        s2 = s1[j - length : j +  length]
        # 去掉#符号
        for i in range(len(s2)):
            if s2[i] != "#":
               res = res + s2[i]
        return res
    # 返回以i为中心的字符串s的最长回文子串的一半的长度
    def central(self, s, i):
        L = i 
        R = i
        while (L >= 0 and R < len(s) and s[L] == s[R] ):
             L = L - 1
             R = R + 1
        return (R-L)//2 - 1


s = Solution()
print(s.longestPalindrome("abba"))
