import heapq
from typing import List
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        heap = []
        # python中默认的堆为 小顶堆 最小的数在堆顶 解决top k问题
        # 如果需要解决 bottom k问题 ，则把原数都取相反数，统一操作
        if k == 0 or k > len(arr) or len(arr) < 1:
            return []        
        for i in range(len(arr)):
            # 入堆k个，初始化堆
            if i < k:
                heapq.heappush(heap,-arr[i])
            else:
            # 如果-arr[i]大于堆顶元素，则入堆，heapreplace，相当于pop+push
                if -arr[i] > heap[0]:
                    heapq.heapreplace(heap,-arr[i])
        res = []
        for i in range(len(heap)):
            res.append(-heapq.heappop(heap))
        # 反向输出list
        return res[::-1]

s = Solution()
print(s.smallestK([1,3,5,7,2,4,6,8],4))
        

             