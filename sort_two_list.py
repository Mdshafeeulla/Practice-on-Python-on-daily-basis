class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged = list1 + list2
        merged.sort()
        print(merged)

new_solution = Solution()
new_solution.mergeTwoLists([1,2,3],[1,2,4])