class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return s in wordDict

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                j = len(word)
                if j <= i and s[i - j : i] == word:
                    dp[i] = dp[i] or dp[i - j]
        return dp[n]
