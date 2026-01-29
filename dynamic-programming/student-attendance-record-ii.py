class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [1, 1, 1, 0, 0, 0]
        # 0 index represents perfect attendance
        # 1 represents one absent
        # 2 represents one late
        # 3 represents two late in row
        # 4 represents one absent, one late
        # 5 represents one absent, two late in row
        
        # dp[x][0] always equals 1
        answer = 3
        mod = 1_000_000_007
        for i in range(1, n):
            dp_copy = dp.copy()
            # Can add a present, late, or absent
            dp[0] = (dp_copy[0] + dp_copy[2] + dp_copy[3]) % mod
            # To get exactly one absent, add absent to anything with exactly no absent or add present to something with one absent and some late
            dp[1] = (dp_copy[0] + dp_copy[1] + dp_copy[2] + dp_copy[3] + dp_copy[4] + dp_copy[5]) % mod
            # To get exactly one late, add late to perfect
            dp[2] = (dp_copy[0]) % mod
            # To get exactly two late in a row, add late to one late
            dp[3] = (dp_copy[2]) % mod
            # To get one absent, one late, add late to one absent
            dp[4] = (dp_copy[1]) % mod
            # To get one absent, two late, add late to one absent, one late
            dp[5] = (dp_copy[4]) % mod
        answer = (dp[0] + dp[1] + dp[2] + dp[3] + dp[4] + dp[5]) % mod
        return answer