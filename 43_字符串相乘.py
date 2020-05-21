# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 示例 1:
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 说明：
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。


# 思路：
# 按位相乘 之后结果相加 用数组会比字符串快
import math

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        len1 = len(num1)
        len2 = len(num2)
        for i in range(len(num1)):
            for j in range(len(num2)):
                index_i = len1 - i - 1
                index_j = len2 - j - 1
                # 这里10的i+j次方用了大数 如果是非python会溢出
                res += int(num1[index_i]) * int(num2[index_j]) * 10**(i + j)
        return str(res)
# 逐个相乘 放到数组里 考虑进位
class Solution2:
    def multiply(self, num1: str, num2: str) -> str:
            num1_len = len(num1)
            num2_len = len(num2)
            res = [0] * (num1_len + num2_len)
            for i in range(num1_len-1,-1,-1):
                for j in range(num2_len-1,-1,-1):
                    tmp = int(num1[i]) * int(num2[j]) + int(res[i+j+1])
                    res[i+j+1] = tmp%10 # 余数作为当前位
                    res[i+j] = res[i+j] + tmp//10 # 前一位加上，进位（商作为进位）
            res = list(map(str, res))
            # print(res)
            for i in range(num1_len+num2_len):
                # print(i)
                if res[i]!='0': # 找到第一个非0数字，后面就是结果
                    return ''.join(res[i:])
            return '0'        
num1 = "123"
num2 = "456"
s = Solution2()
print(s.multiply(num1, num2))


