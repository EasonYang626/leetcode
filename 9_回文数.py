class Solution:
    def isPalindrome(self, x: int) -> bool: 
        string = str(x)
        L = len(string)    
        if L == 0:
            return False       
        if L % 2 == 1:
            i = L//2 - 1
            j = L//2 + 1
            while i >= 0:
                if string[i] == string[j]:
                    i = i - 1
                    j = j + 1
                else:
                    return False
            return True
        if L % 2 == 0:
            i = L//2 - 1
            j = L//2
            while i >= 0:
                if string[i] == string[j]:
                    i = i - 1
                    j = j + 1
                else:
                    return False
            return True        

s = Solution()
print(s.isPalindrome(1))
