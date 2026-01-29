class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = []
        for i in range(len(points)):
            # The number of points is just equal to whatever points is in that cell
            if i == 0:
                dp.append(points[i].copy())
            else:
                new_row = []
                # Need to calculate the max points from previous row
                best_left = []
                best_right = []
                curr_max = float('-inf')
                # The amount of points we can get is the max points plus the diff in positions
                # We can add the current position now and subtract it later
                # When we subtract later, the number we are subtracting will always be larger
                # because we going from the left, meaning indices will be at most j
                for j in range(len(dp[i - 1])):
                    curr_max = max(dp[i - 1][j] + j, curr_max)
                    best_left.append(curr_max)
                
                # Same idea with left, except we will subtract now and add later
                # The reason is that what we are subtracting will be larger than
                # what we are adding because our indices are coming from the right
                curr_max = float('-inf')
                for j in range(len(dp[i - 1]) - 1, -1, -1):
                    curr_max = max(dp[i - 1][j] - j, curr_max)
                    best_right.append(curr_max)
                best_right = best_right[::-1]

                for j in range(len(dp[i - 1])):
                    new_row.append(max(best_left[j] - j, best_right[j] + j) + points[i][j])

                dp.append(new_row)
        return max(dp[-1])
                