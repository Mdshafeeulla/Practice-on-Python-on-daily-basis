class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        if len(nums1) % 2 == 0:
            median1 = len(nums1) / 2
            print(median1)
        else:
            med = len(nums1) / 2
            median = round(med)
            print(nums1[median])



sol = Solution()
sol.findMedianSortedArrays([1,10,22,55,13,11,15,19],[4,1,1])
