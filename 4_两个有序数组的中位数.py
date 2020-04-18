from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int] , nums2: List[int]) -> float:
        mid = (len(nums1)+len(nums2))/2
        mid1 = (len(nums1)+len(nums2))//2
        res = []
        if mid == mid1:
            for i in range(mid1+1):
                if not nums1 and nums2:
                    res.append(nums2.pop(0))
                    continue
                if nums1 and not nums2:
                    res.append(nums1.pop(0))
                    continue
                if nums1[0] > nums2[0]:
                        res.append(nums2.pop(0))
                else:
                        res.append(nums1.pop(0))
            return (res[i-1] + res[i])/2    
        else:
            for i in range(mid1+1):
                if not nums1 and nums2:
                    res.append(nums2.pop(0))
                    continue
                if nums1 and not nums2:
                    res.append(nums1.pop(0))
                    continue
                if nums1[0] > nums2[0]:
                        res.append(nums2.pop(0))
                else:
                        res.append(nums1.pop(0))
            return res[i]

s = Solution()
nums1 = [1,2, 3]
nums2 = []
print(s.findMedianSortedArrays(nums1,nums2))