class Solution:
    def longestValidParentheses(self, s: str) -> int:
        for i in range(0,len(s) - 1):
            count = 0
            if s[i] == s[i + 1] :
                count += 2
                print(count)
            else:
                count = 0
            print(count)

sol = Solution()
sol.longestValidParentheses("{{}}")