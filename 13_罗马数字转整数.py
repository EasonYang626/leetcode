# 思路 字典存储 key是罗马数字 value是对应的数值
# 遍历 string 如果当前罗马数字对应的值 小于 之后的罗马数字对应的值
# 则结果上 要减去当前罗马数字对应的值 否则 加上该值
# 例如 IV 读入I 之后发现V 对应的值大于I 则减去I对应的值
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,
               'V':5,
               'X':10,
               'L':50,
               'C':100,
               'D':500,
               'M':1000}
        res = 0
        for i in range(len(s) - 1):
            if dic[s[i]] < dic[s[i + 1]]:
                res = res - dic[s[i]]
            else:
                res = res + dic[s[i]]
        # 对最后一个字符单独处理 直接加上它对应的值即可 放到前面会越界
        res = res + dic[s[-1]]
        return res
s = Solution()
print(s.romanToInt("MCMXCIV"))
