class Solution(object):
    def palindrome(self,n):
        n = str(n)
        if n == n[::-1]:
            print(f"The given string is Palindrome:{n}")
        else:
            print(f"The given string is not Palindrome :{n}")

new_solution = Solution()
new_solution.palindrome('racecar')