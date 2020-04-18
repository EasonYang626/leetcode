import math
class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        res = 0
        fushu = 1
        pop = 0       
        if x < 0:
            x = x * -1
            fushu = -1
        while flag :
            pop = x % 10
            x = x // 10
            if x == 0:
                flag = 0
            res = res * 10 + pop
        if int(res * fushu) < math.pow(-2,31) or int(res * fushu) > math.pow(2,31) - 1 :
            return 0
        return int(res * fushu)
s = Solution()
print(s.reverse(123))