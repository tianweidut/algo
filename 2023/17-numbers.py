class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        letters = [letter_map[d] for d in digits]
        results = []

        def dfs(start: int, result: str):
            if start == len(letters):
                return

            for letter in letters[start]:
                result += letter
                if len(result) == len(letters):
                    results.append(result)
                dfs(start + 1, result)
                result = result[:-1]

        dfs(0, "")
        return results
