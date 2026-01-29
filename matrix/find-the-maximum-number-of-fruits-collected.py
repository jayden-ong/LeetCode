class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        # Child (0, 0) must move right and down
        # Child (0, n - 1) must move down (can move left, right or straight)
        # Child (n - 1, 0) must move right (can move up, down or straight)

        # Child (0, 0) has to move diagonally?
        # Child cannot cross the diagonal
        answer = 0
        dp = []
        dp2 = []
        for i in range(len(fruits)):
            answer += fruits[i][i]
            fruits[i][i] = 0
            dp.append([0] * len(fruits))
            dp2.append([0] * len(fruits))
        dp[-1][0] = fruits[-1][0]
        # Can only go up a maximum of (len(fruits) - 1) // 2 times and for every time you go up, must go down
        up_times = 1
        for j in range(1, len(fruits)):
            for i in range(len(fruits) - 1, len(fruits) - 2 - up_times, -1):
                curr_max = 0
                if i < len(fruits) - 1:
                    curr_max = max(curr_max, dp[i + 1][j - 1])
                curr_max = max(curr_max, dp[i][j - 1])
                # In case we came from a higher tile -- if tile is unreachable, this won't matter since it will be 0
                curr_max = max(curr_max, dp[i - 1][j - 1])
                dp[i][j] = fruits[i][j] + curr_max
                
            if len(fruits) % 2 == 0:
                if j < len(fruits) // 2 - 1:
                    up_times += 1
                elif j >= len(fruits) // 2:
                    up_times -= 1
            else:
                if j < len(fruits) // 2:
                    up_times += 1
                elif j >= len(fruits) // 2:
                    up_times -= 1

        answer += dp[-1][-1]
        dp2[0][-1] = fruits[0][-1]
        left_times = 1
        for i in range(1, len(fruits)):
            for j in range(len(fruits) - 1, len(fruits) - 2 - left_times, -1):
                curr_max = 0
                if j < len(fruits) - 1:
                    curr_max = max(curr_max, dp2[i - 1][j + 1])
                curr_max = max(curr_max, dp2[i - 1][j])
                # In case we came from a higher tile -- if tile is unreachable, this won't matter since it will be 0
                curr_max = max(curr_max, dp2[i - 1][j - 1])
                dp2[i][j] = fruits[i][j] + curr_max
                
            if len(fruits) % 2 == 0:
                if i < len(fruits) // 2 - 1:
                    left_times += 1
                elif i >= len(fruits) // 2:
                    left_times -= 1
            else:
                if i < len(fruits) // 2:
                    left_times += 1
                elif i >= len(fruits) // 2:
                    left_times -= 1
        answer += dp2[-1][-1]
        return answer