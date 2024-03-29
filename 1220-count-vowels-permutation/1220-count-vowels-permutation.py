class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[ 0 for _ in range(5)] for _ in range(n)]
        for j in range(5):
            dp[0][j] = 1
        for i in range(1, n):
            for j in range(5):
                dp[i][0] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]
                dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
                dp[i][2] = dp[i - 1][1] + dp[i - 1][3]
                dp[i][3] = dp[i - 1][2]
                dp[i][4] = dp[i - 1][2] + dp[i - 1][3]

        sol = sum(dp[-1])
        return sol % (10 ** 9 + 7)