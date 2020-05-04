import re


class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        str = str.lstrip()
        num_re = re.compile(r'^[\+\-]?\d+')
        str.lstrip()
        # /^A/会匹配"An e"中的A，但是不会匹配"ab A"中的A
        # []范围限定符 \用来转义 \d匹配数字 +是贪婪 匹配后面一个或多个
        num = re.findall(num_re, str)
        num = int(*num)  # 由于返回的是个列表，解包并且转换成整数
        # zip()压缩可迭代对象，*号解压可迭代对象
        # 可迭代对象才可以使用*号拆分；
        # 带*号变量严格来说并不是一个变量，而更应该称为参数，它是不能赋值给其他变量的，但可以作为参数传递
        return max(min(num, INT_MAX), INT_MIN)  # 返回值


s = Solution()
print(s.myAtoi('dwa132 464dw123 *&%12'))
