class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        # Start with the first string as the initial common prefix.
        prefix = strs[0]

        # Iterate through the rest of the strings in the list.
        for i in range(1, len(strs)):
            # The main logic lies here like
            # 'a'.find('a') will return 0
            #if it is not same it will return -1
            #Here the while loop runs until it is true,so if it find out the substring it will return 0
            #And the loop breaks
            while strs[i].find(prefix) != 0:
            #Here we are reassinging the value of prefix
            #And also cutting the last word for the list
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        # After the loop, the remaining prefix is the longest common one.
        return prefix

new_solution = Solution()

# Store the result in a variable
result = new_solution.longestCommonPrefix(strs=['asns', 'asds', 'adcs'])
print(result)