class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines_set = set()
        for mine in mines:
            mines_set.add(tuple(mine))
        
        dp = []
        for i in range(n):
            new_row = []
            for j in range(n):
                new_row.append([])
            dp.append(new_row)
        
        answer = 0
        # Only for horizontal
        for i in range(n):
            curr_ones_left = 0
            # Going left
            for j in range(n):
                if (i, j) not in mines_set:
                    curr_ones_left += 1
                    dp[i][j].append(curr_ones_left)
                else:
                    dp[i][j].append(0)
                    curr_ones_left = 0
            
            curr_ones_right = 0
            # Going right
            for j in range(n - 1, -1, -1):
                if (i, j) not in mines_set:
                    curr_ones_right += 1
                    dp[i][j].append(curr_ones_right)
                else:
                    dp[i][j].append(0)
                    curr_ones_right = 0
        
        # Only for vertical
        for j in range(n):
            curr_ones_up = 0
            # Going up
            for i in range(n):
                if (i, j) not in mines_set:
                    curr_ones_up += 1
                    dp[i][j].append(curr_ones_up)
                else:
                    dp[i][j].append(0)
                    curr_ones_up = 0
            
            curr_ones_down = 0
            # Going down
            for i in range(n - 1, -1, -1):
                if (i, j) not in mines_set:
                    curr_ones_down += 1
                    dp[i][j].append(curr_ones_down)
                else:
                    dp[i][j].append(0)
                    curr_ones_down = 0
        
        for i in range(n):
            for j in range(n):
                answer = max(answer, min(dp[i][j]))
        return answer