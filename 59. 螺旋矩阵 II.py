from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        up = 0
        down = n - 1
        left = 0
        right = n - 1
        res = [[0 for i in range(n)] for j in range(n)]
        x = 1
        while True:
            for i in range(left, right + 1):
                res[up][i] = x
                x += 1
            up += 1
            if up > down:
                return res
            for i in range(up, down + 1):
                res[i][right] = x
                x += 1
            right -= 1
            if right < left:
                return res
            for i in range(right, left - 1, -1):
                res[down][i] = x
                x += 1
            down -= 1
            if down < up:
                return res
            for i in range(down, up - 1, -1):
                res[i][left] = x
                x += 1
            left += 1
            if left > right:
                return res
