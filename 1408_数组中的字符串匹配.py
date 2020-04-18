from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [s for s in words if any(i!=s and len(s) < len(i) and s in i for i in words)]
        # 提前判断长度s是否小于i，简化不必要的s in i判断