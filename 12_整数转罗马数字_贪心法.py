class Solution:
    def intToRoman(self, num: int) -> str:
        # 把阿拉伯数字与罗马数字可能出现的所有情况和对应关系，放在两个数组中
        # 并且按照阿拉伯数字的大小降序排列，这是贪心选择思想
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        index = 0
        res = ''
        while index < 13:
            while num >= nums[index]:
                #等于号 贪心法 选择尽可能大的数 类似于钞票面额 用最少的钞票 兑换等价面额
                res = res + romans[index]
                num = num - nums[index]
            index = index + 1
        return res

s = Solution()
print(s.intToRoman(1994))     
