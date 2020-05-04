class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        res = ""
        row = 1
        i = numRows
        j = 0 
        if i == 1:
            return s
        while row <= i:
            if row > length:
                break
            if row == 1 or row == i:
                res = res + s[row-1]
                j = row
                while j + 2 * i - 2 <= length:
                    j = j + 2 * i -2
                    res = res + s[j-1]
            
            else:
                res = res + s[row-1]
                j = row
                while j + 2 * i - row * 2 <= length:
                    j = j + 2 * i - row * 2
                    res = res + s[j-1]
                    if j + 2 * row -2 <= length:
                        j = j + 2 * row -2
                        res = res + s[j-1]
                    else:
                        break
            row = row + 1
        return res
# 维护min(numRows,len(s))个数的列表，遍历字符串中的字符，
# 根据向上或向下的方向将字符加入对应的行的列表中，到达首行或尾行，则改变方向
s = Solution()
print(s.convert("A",2))
