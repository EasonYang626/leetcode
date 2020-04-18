import math
class Solution:
    def myAtoi(self, str: str) -> int:
        a = ''
        b= []
        flag = True
        flag2 = True
        fuhao = ''
        if str == '':
            return 0
        for i in str:
            if i == ' ' and flag:
                continue
            if (i =='-' or i == '+') and flag:
                fuhao = i
                flag = False
                continue
            flag = False
            # 结束前面判断非符号和正负号之后 后面不再进行判断
            if not self.isNum(i) and flag2:
                return 0
            # 结束前面的判断后还遇到非数字 如'+ s'
            if not self.isNum(i) and not flag2:
                break
            # 已经遇到数字后 再遇到非数字直接结束
            if self.isNum(i):
                b.append(i)
                flag2 = False
                # 第一次判断到是数字，之后将flag2置为false，不再进行非数字则返回0的操作
                continue
        if len(b) == 0:
            return 0
        # 全都是' '或者其他没有读取到数字的情况
        if fuhao == '-':
            if int(a.join(b)) > math.pow(2,31):
                return int(math.pow(2,31) * -1)
            return int(a.join(b)) * -1
        if int(a.join(b)) > math.pow(2,31) -1:
            return int(math.pow(2,31) -1) 
            # 注意不加int返回的是浮点数
        return int(a.join(b))

    def isNum(self,c):
        if c >= '0' and c <= '9':
            return True
        else:
            return False

s = Solution()
print(s.myAtoi("-42"))