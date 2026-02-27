import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        if len(nums1) % 2 == 0:
            median = len(nums1) / 2
            print(nums1[int(median)],nums1[int(median - 1)])
        else:
            med = len(nums1) / 2
            median = math.ceil(med)
            print(nums1[median - 1])



sol = Solution()
sol.findMedianSortedArrays([1,1,4,2,6,8],[4,3])
