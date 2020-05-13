# 回溯法
from typing import List

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def check(x, y, s):
            # 检查对应的行列里有没有S
            for i in range(9):
                if board[i][y] == s or board[x][i] == s:
                    return False
            # 检查对应的box里有没有S
            for i in [0, 1, 2]:
                for j in [0, 1, 2]:
                    if board[x//3*3+i][y//3*3+j] == s:
                        return False
            return True
        
        def bt(cur):
            if cur == 81:
                return True
            x, y = cur // 9, cur % 9
            # 如果当前位置已经填好了数
            if board[x][y] != '.':
                return bt(cur + 1)
            for i in range(1, 10):
                s = str(i)
                if check(x, y, s):
                    board[x][y] = s
                    # 如果下一个元素也可以填好
                    if bt(cur + 1):
                        return True
                    # 否则回溯
                    board[x][y] = '.'
            return False
        
        bt(0)

s = Solution()
s.solveSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]])