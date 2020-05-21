# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 每一个解释前一个 2.就是有一个1  即11
# 3. 有两个1 即21

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(1)
        # 保存上一步的结果
        before = self.countAndSay(n - 1)
        res = ""
        i = 0
        count = 0
        while i < len(before): 
            count = 1
            # 统计有多少个相同的数字连续挨着
            while i + 1 < len(before):
                if before[i + 1] == before[i]:
                    count += 1
                    i += 1
                else:
                    break
            
            res = res + (str(count)) + before[i]
            # 跳到下一个不一样的数字
            i += 1
        return res
s = Solution()
print(s.countAndSay(5))


