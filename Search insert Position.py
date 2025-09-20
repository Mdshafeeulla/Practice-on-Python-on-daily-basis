#The code uses a linear search for elements untill it find outs the correct match if not it
#will iterate untill the last
class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        #If the element(target) is greater than entire list given we will by default print the
        #length of the list
        return len(nums)



# Test cases to verify the corrected logic.
search_solution = Solution()

# Example 1: Target is in the array.
nums1 = [1, 3, 5, 6]
target1 = 7
print(f"Input: {nums1}, Target: {target1}")
print(f"Output: {search_solution.searchInsert(nums1, target1)}")  # Expected Output: 2
print("-" * 20)
