def tri_path(tri):
    if not tri:
        return 0

    m = len(tri)
    dp = [[0 for j in range(i+1)] for i in range(m)]
    dp[0][0] = tri[0][0]

    for i in range(1, m):
        for j in range(0, i + 1):
            if j == 0:
                x = dp[i-1][j]
            elif j >= len(tri[i-1]):
                x = dp[i-1][j-1]
            else:
                x = min(dp[i-1][j-1], dp[i-1][j])
            dp[i][j] = x + tri[i][j]

    return min(dp[-1])

if __name__ == "__main__":
    x = tri_path([[2], [3,4], [6,5,7], [4,1,8,3]])
    print(x)
