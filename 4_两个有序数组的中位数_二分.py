from typing import List


class Solution:

    def getKth(self,nums1, start1, end1, nums2, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        # 始终保持len1小于len2 len1最先为0
        if len1 > len2:
            return self.getKth(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0:
            return nums2[start2 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])
        # 取两个数组的第k//2小的数作比，如果超过数组本身，则取数组最后一个数
        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1
        # 比较小的那个数组的前面k//2个都排除
        if nums1[i] > nums2[j]:
            return self.getKth(nums1, start1, end1, nums2, j + 1, end2, k - min(len2, k // 2))
        else:
            return self.getKth(nums1, i + 1, end1, nums2, start2, end2, k - min(len1, k // 2))

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        # 统一奇偶操作
        left = (n + m + 1) // 2
        right = (n + m + 2) // 2
        return (self.getKth(nums1, 0, n - 1, nums2, 0, m - 1, left) + self.getKth(nums1, 0, n - 1, nums2, 0, m - 1, right)) / 2


s = Solution()
nums1 = [1]
nums2 = [2,3,4,5,6]
print(s.findMedianSortedArrays(nums1, nums2))