class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for ch in s:
            if ch in ['(','[','{']:
                stack.append(ch)
            if ch == ')' :
                if not stack:
                    return False
                if stack.pop() != '(':
                    return False
            if ch == ']' :
                if not stack:
                    return False                
                if stack.pop() != '[':
                    return False            
            if ch == '}' :
                if not stack:
                    return False                
                if stack.pop() != '{':
                    return False
        if stack:
            return False
        return True
# 另一种思路 如果串合法 每次去掉最里面的一对 最终会成空串
class Solution2:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
        
s = Solution()
print(s.isValid(']'))
