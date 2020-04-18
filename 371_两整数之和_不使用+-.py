# 位运算 
# 分为低位和进位
# 低位为两数的异或结果^
# 进位为两数的与&结果，这里需要左移一位
# 之后低位和进位再做异或，与运算，再得到新的低位和进位
# 重复以上过程直到进位为0
class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 1
        low = 0
                # 2^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF 
        MIN_INT = MAX_INT + 1
        # 对应二进制中31个1
        if a == 0:
            return b
        if b == 0:
            return a
        while a != 0:
            carry = (a & b) << 1
            low = a ^ b
            a = carry % MASK
            b = low % MASK
        return b if b <= MAX_INT else ~((b % MIN_INT) ^ MAX_INT)
        # 在 Python 中的特殊处理
        # 在 Python 中，整数不是 32 位的，
        # 也就是说你一直循环左移并不会存在溢出的现象，
        # 这就需要我们手动对 Python 中的整数进行处理，手动模拟 32 位 INT 整型。
        # 具体做法是将整数对 0x100000000 取模，保证该数从 32 位开始到最高位都是 0。



s = Solution()
print(s.getSum(-5,-5))
