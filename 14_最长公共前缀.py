from typing import List
class Solution:
    def longestCommonPrefix(self, strs) :
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        dic = {i:ch for i,ch in enumerate(strs[0])}
        dic1 = {}
        res = ''
        # 排除第一个
        # 注意 字典中的 key不能重复 是唯一的 可能会出现'aa'等情况
        for one_str in strs[1:]:
            # dic = {i:ch for i,ch in enumerate(str) if ch == dic[i]} 会越界 原字典是flow 新字符串是flight的情况下
            for i,ch in enumerate(one_str):
                if i > len(dic.keys()) - 1:
                    break
                if ch == dic[i]:
                    dic1[i] = ch
                else:
                    break
            dic = dic1
            dic1 = {}
            # dic1.clear() 没赋值 直接操作clear 此时dic1 和 dic均指向同一片包含新字典的地址空间
            # clear之后 dic 和 dic1 都会指向 空字典{}
        for ch in dic.values():
            res = res + ch
        return res
s = Solution()
print(s.longestCommonPrefix(["aca","cba"]))