# This solution follows a stack LIFO
from Palindrome import new_solution


class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            #In this it will check the key like '}' not for opening bracket
            #It will search for the key in mapping that is why we have used key as the closing brackets
            # Logic behind this
            # map = {1: 'Shafi', 2: 'Md'}
            # name = 1
            # if name in map:
            #     print("True")
            # else:
            #     print("False")
            if char in mapping:
                #Here we are using the '#' to get rid of indexerror if no element is present
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return True


new_solution = Solution()
print(new_solution.isValid('()[]{}'))
print(new_solution.isValid('(]'))
print(new_solution.isValid('([)]'))