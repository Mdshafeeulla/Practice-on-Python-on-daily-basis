class Solution:
    def longestValidParentheses(self, s: str) -> int:
        match = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        count = 0
        for i in range(0,len(s) - 1):
            for exact_match in match:
                if s[i] == exact_match and s[i + 1] == match[exact_match]:
                    count += 2
                else:
                    count += 0
        print(count)



sol = Solution()
sol.longestValidParentheses("[{}[]}")