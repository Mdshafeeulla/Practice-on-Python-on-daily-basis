class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)

sol = Solution()
sol.findMedianSortedArrays([1,2,3],[4,3,2])
