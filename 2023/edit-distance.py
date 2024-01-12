
    def min_distance(self, w1, w2):
        # word1 = "horse", word2 = "ros"  3
        m = len(w1)
        n = len(w2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, n + 1):
            dp[0][i] = i

        for i in range(1, m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if w1[i - 1] == w2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],  # replace
                        dp[i][j - 1],  # insert
                        dp[i - 1][j],  # remove
                    )

        return dp[m][n]
