class Solution:
    def intToRoman(self, num: int) -> str:
        M = num // 1000
        num = num % 1000
        res = ''
        for i in range(M):
            res = res + 'M'
        if num // 100 == 9:
            res = res + 'CM'
            num = num % 100
        if num // 100 == 4:
            res = res + 'CD'
            num = num % 100
        if 0 < num // 100 < 5:
            for i in range(num // 100):
                res = res + 'C'
            num = num % 100
        if num // 100 > 4:
            res = res + 'D'
            for i in range(num//100 - 5):
                res = res + 'C'
            num = num % 100
        if num // 10 == 9:
            res = res + 'XC'
            num = num % 10
        if num // 10 == 4:
            res = res + 'XL'
            num = num % 10
        if 0 < num // 10 < 5:
            for i in range(num // 10):
                res = res + 'X'
            num = num % 10
        if num // 10 > 4:
            res = res + 'L'
            for i in range(num//10 - 5):
                res = res + 'X'
            num = num % 10
        if num  == 9:
            res = res + 'IX'
            num = 0
        if num  == 4:
            res = res + 'IV'
            num = 0
        if 0 < num  < 5:
            for i in range(num):
                res = res + 'I'
            num = 0
        if num > 4:
            res = res + 'V'
            for i in range(num - 5):
                res = res + 'I'   
            num = 0 
        return res

s = Solution()
print(s.intToRoman(1994))     