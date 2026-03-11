class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        num_to_letters ={
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        print(num_to_letters)

comb = Solution
comb.letterCombinations("123")