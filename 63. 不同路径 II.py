from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        # 如果起始位置就是障碍的情况
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        # 处理最上边和最左边的情况
        # 最左边的话，如果出现了一个障碍，则障碍及障碍下边的所有点都不可到达
        for i in range(1, m, 1):
            if obstacleGrid[i][0] == 1:
                for j in range(i, m, 1):
                    dp[j][0] = 0
                break
            else:
                dp[i][0] = 1
        # 最上边的话，如果出现了一个障碍，则障碍及障碍右边的所有点都不可到达
        for i in range(1, n, 1):
            if obstacleGrid[0][i] == 1:
                for j in range(i, n, 1):
                    dp[0][j] = 0
                break
            else:
                dp[0][i] = 1
        # 边界处理完，处理内部
        for i in range(1, m, 1):
            for j in range(1, n, 1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


# 同一思路的更简便的写法
class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j - 1]
                    elif j == 0:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


s = Solution()
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
