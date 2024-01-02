class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        max_len = 0
        max_substr = s[0]

        for sub_len in range(2, n + 1):
            for start in range(0, n):
                # sub_len = end - start + 1
                end = sub_len + start - 1

                if end >= n:
                    break

                if s[start] == s[end]:
                    if sub_len <= 2:
                        dp[start][end] = True
                    else:
                        dp[start][end] = dp[start + 1][end - 1]
                else:
                    dp[start][end] = False

                if dp[start][end] and sub_len > max_len:
                    max_len = sub_len
                    max_substr = s[start : end + 1]

        return max_substr
