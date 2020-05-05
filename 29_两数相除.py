# 举个例子：11 除以 3 。
# 首先11比3大，结果至少是1， 然后我让3翻倍，就是6，
# 发现11比3翻倍后还要大，那么结果就至少是2了，
# 那我让这个6再翻倍，得12，11不比12大，吓死我了，差点让就让刚才的最小解2也翻倍得到4了。
# 但是我知道最终结果肯定在2和4之间。也就是说2再加上某个数，这个数是多少呢？
# 我让11减去刚才最后一次的结果6，剩下5，我们计算5是3的几倍，也就是除法，看，递归出现了
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。
# 本题中，如果除法结果溢出，则返回 2^31 − 1。
import math 

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 除数不为0
        if divisor == 0:
            return None
        # 符号位
        sign = 1
        # 越界情况直接特判 只可能发生在-2^31 / -1 时
        if dividend == -math.pow(2, 31) and divisor == -1:
            return int(math.pow(2, 31) - 1)
        # 俩数都小于0的情况
        if dividend < 0 and divisor < 0:
            dividend = 0 - dividend
            divisor = 0 - divisor
        # 只有一个小于0的情况
        if dividend < 0 and divisor > 0:
            dividend = 0 - dividend
            sign = -1
        if dividend > 0 and divisor < 0:
            divisor = 0 - divisor
            sign = -1    

        # 被除数小于除数直接返回0
        if dividend < divisor:
            return 0
        # 被除数等于除数返回1 这里还要考虑符号位
        if dividend == divisor:
            return sign
        res = 1
        pre = 0
        divisor1 = divisor
        divisor1 = divisor1 + divisor1
        # 看除数的两倍有没有被除数大
        while divisor1 <= dividend:
            # pre保存原被除数减去最后一次的除数的结果
            pre = dividend - divisor1
            divisor1 = divisor1 + divisor1
            # 每当执行了一次循环 就说明除数的二倍还是小于被除数 商就起码是原来的二倍
            res = res + res
        # 11除以3  12比11大了 返回2 + divide(11 - 6, 3)
        # divide(5, 3) = 1 + divide(2, 3) = 1 + 0 = 1
        res = res + self.divide(pre, divisor)
        if sign < 0:
            res = 0 - res
        return int(res)
s = Solution()
print(s.divide(15, 2))

