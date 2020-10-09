from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        res = []
        sum = m * n
        i = 0
        j = 0
        k = 0
        while sum > 0:
            while j < n - k:
                res.append(matrix[i][j])
                sum -= 1
                j += 1
                if sum == 0:
                    return res
            j -= 1
            i += 1
            while i < m - k:
                res.append(matrix[i][j])
                sum -= 1
                i += 1
                if sum == 0:
                    return res
            i -= 1
            j -= 1
            while j > k - 1:
                res.append(matrix[i][j])
                sum -= 1
                j -= 1
                if sum == 0:
                    return res
            j += 1
            i -= 1
            while i > k:
                res.append(matrix[i][j])
                sum -= 1
                i -= 1
                if sum == 0:
                    return res
            i += 1
            j += 1
            k += 1

# 对于这种螺旋遍历的方法，重要的是要确定上下左右四条边的位置，
# 那么初始化的时候，上边up就是0，下边down就是m-1，左边left是0，
# 右边right是n-1。然后我们进行while循环，先遍历上边，将所有元素加入结果res，
# 然后上边下移一位，如果此时上边大于下边，说明此时已经遍历完成了，直接break。
class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        res = []
        up = 0
        down = m - 1
        left = 0
        right = n - 1
        while True:
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
            if down < up:
                break
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if ++left > right:
                break
        return res


s = Solution2()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
