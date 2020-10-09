import re


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pattern = re.compile(r'[^\s]+$')
        word = re.findall(pattern, s)
        if len(word) == 0:
            return 0
        else:
            return len(word[0])

class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip(' ')
        L = s.split(' ')[-1]
        return len(L)

s = Solution()
print(s.lengthOfLastWord("a"))
