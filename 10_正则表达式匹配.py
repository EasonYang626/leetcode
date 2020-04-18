class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 递归 递归式 + 递归出口 递归处理好当前 不管后面
        if not p:    #p为空 且 s 为空 则返回true
            return not s
        f_match = bool(s) and (p[0] in (s[0] , '.')) 
        # s 如果为空 f_match直接为false 不会进行后面的判断 也就不会越界      
        if len(p) >= 2 and p[1] == '*':
        #    有*出现的情况 分两种 
        # * 代表的是该字符出现0次 则s不动 p跳过该字符和*
        # * 代表该字符出现一次或多次 递归里只需要考虑一次 则在该字符匹配上的前提下 
        # s跳过当前字符 p不动
            return self.isMatch(s,p[2:]) or (f_match and self.isMatch(s[1:],p))
            # 把上面的两个分别 赋值给 A 和 B
            # 再return A or B 会大大增加时间 因为第一个如果是true则直接返回了 不会计算第二个
            # 这样写就都会计算到头

        else:
            # 没有* 在该字符匹配上的前提下 s 和 p都跳一个
            return f_match and self.isMatch(s[1:],p[1:])

        
s = Solution()
print(s.isMatch('aaaa','a*'))