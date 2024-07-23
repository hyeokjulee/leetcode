class Solution:
    def letterCombinations(self, digits):
        result = []
        number_words = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backTracking(idx, letter):
            if idx < len(digits):
                for word in number_words[digits[idx]]:
                    backTracking(idx + 1, letter + word)
            elif len(letter) > 0:
                result.append(letter)

        backTracking(0, "")
        
        return result