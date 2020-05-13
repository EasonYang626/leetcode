from typing import List
# 思路：哈希表存储 key存储单词 value存储出现次数
# 滑动窗口 假设单词长度固定为4 
# 则从0开始每次窗口内包含S长度的字符串 每次读入4个字符 检查是否在哈希表中
# 当前窗口可以则返回左窗口位置
# 不行 则窗口整体向前移动4个位置
# 把上述循环再 从1 2 3开始分别做一下
# 这样就包含了所有的情况
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        # 统计每个单词出现的频率 存入Counter类似字典
        words_map = Counter(words)
        cur_map = Counter()
        oneword = len(words[0])
        n_word = oneword * len(words)
        # 总长度还没一个单词大
        if len(s) < oneword:
            return []
        res = []
        # 最外层循环 
        for i in range(oneword):
            left = i
            right = i
            # 当左窗口加上n个单词总长 小于等于 s总长时 则有可能有解
            while left + n_word <= len(s):
                # 当前窗口长度只要小于等于n个单词总长 就继续循环 增加窗口长度
                while right - left <= n_word:
                    cur_word = s[right: right + oneword]
                    # 可以引用cur_map中不存在元素 出现次数默认为0
                    if cur_word in words_map and cur_map[cur_word] < words_map[cur_word]:
                        cur_map[cur_word] += 1
                        right += oneword
                        # 窗口长度等于n个单词长总和 则找到一个符合要求的
                        if right - left == n_word:
                            res.append(left)
                            cur_map.clear()
                            break
                    else:
                        # 下次循环前 清空cur_map
                        cur_map.clear()
                        break   

                left += oneword
                right = left
                # 结束循环 或者返回了一个结果 或者无解
                # 都需要把right left置为相同的值
                
        return res
# 这里主要的区别在于回溯
# 如果当前单词 不在words中 则直接回溯到当前单词的后面 跳过该单词
# 否则遇到该单词 还是无解
# 如果该单词在 words中 但是次数超出了已有的
# 则从左边窗口弹出一个单词 已匹配单词数减一 
# 重复这个循环 直到次数不超限了
# 这里主要考虑到 左边还有当前单词 如果直接简单的跳过 会丢解
class Solution2:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        words_len = one_word * word_num
        n = len(s)
        if n < words_len:return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            # 只要左窗口加上总单词长度 小于等于字符串长度 就继续循环
            while left + words_len <= n:
                w = s[right:right + one_word]
                right += one_word
                # 不在words中 直接跳过
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    # 次数超限的情况 从左窗口弹出单词
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    # 直接用已匹配单词数 是否等于 总单词数 来判断是否为一个解
                    if cur_cnt == word_num :
                        res.append(left)
        return res


s= Solution()
print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))