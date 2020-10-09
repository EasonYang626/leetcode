from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按数组中的第一个元素排序
        # [2, 6], [8, 10], [1, 3], [15, 18], [5, 8], [2, 4]
        # [1, 3], [2, 4], [2, 6], [5, 8], [8, 10], [15, 18]
        # 这样就保证了 后面的区间的第1个数一定大于前面的区间的第1个数
        # 之后比较 后面的区间的第1个数和前面的区间的第2个数
        # 如果小于前面区间的第2个数，则说明有交集
        # 结果区间的第二个数改为 前面区间和后面区间的第二个数中 较大的那个
        # 2<3 -> 有交集 -> 比较3和4 -> 区间变为[1, 4]
        intervals = sorted(intervals)
        res = []
        for each in range(len(intervals)):
            if res == [] or intervals[each][0] > res[-1][1]:
                res.append(intervals[each])
            else:
                res[-1][1] = max(intervals[each][1], res[-1][1])
        return res


s = Solution()
print(s.merge([[2, 6], [8, 10], [1, 3], [15, 18], [5, 8], [2, 4]]))
