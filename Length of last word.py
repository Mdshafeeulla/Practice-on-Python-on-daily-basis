class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        if not words:
            return 0
        #Here the -1 print the last word
        return len(words[-1])


len_solution = Solution()
result = len_solution.lengthOfLastWord("my name is")
print(result)