# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，
# 并且使皇后彼此之间不能相互攻击
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 示例:
# 输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。



import copy
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        empty_row = ['.'] * n
        board = []
        for i in range(n):
            board.append(empty_row.copy())
        res = []
        # 判断在第x行y列能否放Q
        def check(x, y):
            # 由于我们递归直接是下一行 可以跳过判断行
            # 判断列
            for i in range(x):
                if 'Q' == board[i][y]:
                    return False
            # 判断对角线
            # 判断当前行之上的行
            for i in range(1, x + 1):
                if y + i < n and x - i >=0 and 'Q' == board[x - i][y + i]:
                    return False
                if y - i >= 0 and x - i >=0 and 'Q' == board[x - i][y - i]:
                    return False    
            # 判断当前行之下的行 由于我们是按行向下求解 所以下面的行不需要考虑
            return True

        def backtrace(x):
            if x == n:
                string_board = []
                for i in board:
                    string_board.append(''.join(i))
                res.append(string_board)            
                return
            for i in range(n):
                if check(x, i):
                    board[x][i] = 'Q'
                    backtrace(x + 1)                                          
                    # 回溯
                    board[x][i] = '.'
        backtrace(0)
        return res

s = Solution()
print(s.solveNQueens(5))

