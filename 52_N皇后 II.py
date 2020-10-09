class Solution:
    def totalNQueens(self, n: int) -> int:
        empty_row = ['.'] * n
        board = []
        for i in range(n):
            board.append(empty_row.copy())
        self.res = 0

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
                if y + i < n and x - i >= 0 and 'Q' == board[x - i][y + i]:
                    return False
                if y - i >= 0 and x - i >= 0 and 'Q' == board[x - i][y - i]:
                    return False
                    # 判断当前行之下的行 由于我们是按行向下求解 所以下面的行不需要考虑
            return True

        def backtrace(x):
            if x == n:
                self.res += 1
                return
            for i in range(n):
                if check(x, i):
                    board[x][i] = 'Q'
                    backtrace(x + 1)
                    # 回溯
                    board[x][i] = '.'

        backtrace(0)
        return self.res


s = Solution()
print(s.totalNQueens(5))
