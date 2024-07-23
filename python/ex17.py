class Solution:
    def letterCombinations(self, digits):
        result = []
        n = len(digits)

        def backTracking(idx, letter):
            if idx != n:
                if digits[idx] == "2":
                    backTracking(idx + 1, letter + "a")
                    backTracking(idx + 1, letter + "b")
                    backTracking(idx + 1, letter + "c")
                if digits[idx] == "3":
                    backTracking(idx + 1, letter + "d")
                    backTracking(idx + 1, letter + "e")
                    backTracking(idx + 1, letter + "f")
                if digits[idx] == "4":
                    backTracking(idx + 1, letter + "g")
                    backTracking(idx + 1, letter + "h")
                    backTracking(idx + 1, letter + "i")
                if digits[idx] == "5":
                    backTracking(idx + 1, letter + "j")
                    backTracking(idx + 1, letter + "k")
                    backTracking(idx + 1, letter + "l")
                if digits[idx] == "6":
                    backTracking(idx + 1, letter + "m")
                    backTracking(idx + 1, letter + "n")
                    backTracking(idx + 1, letter + "o")
                if digits[idx] == "7":
                    backTracking(idx + 1, letter + "p")
                    backTracking(idx + 1, letter + "q")
                    backTracking(idx + 1, letter + "r")
                    backTracking(idx + 1, letter + "s")
                if digits[idx] == "8":
                    backTracking(idx + 1, letter + "t")
                    backTracking(idx + 1, letter + "u")
                    backTracking(idx + 1, letter + "v")
                if digits[idx] == "9":
                    backTracking(idx + 1, letter + "w")
                    backTracking(idx + 1, letter + "x")
                    backTracking(idx + 1, letter + "y")
                    backTracking(idx + 1, letter + "z")
            elif len(letter) != 0:
                result.append(letter)

        backTracking(0, "")
        
        return result