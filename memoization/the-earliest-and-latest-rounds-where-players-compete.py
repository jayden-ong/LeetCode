class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        # If firstPlayer == n - secondPlayer + 1, maybe answer is [1, 1]?
        def solve(num_players, curr_first, curr_second):
            if curr_first + curr_second == num_players + 1:
                return [1, 1]
            if curr_first > curr_second:
                curr_first, curr_second = curr_second, curr_first
            if num_players <= 4:
                return [2, 2]
            
            next_round_players = (num_players + 1) // 2
            curr_early, curr_late = float('inf'), float('-inf')

            # Because players are changing position, need to adjust the player numbers
            if curr_first - 1 > num_players - curr_second:
                temp = num_players + 1 - curr_first
                curr_first = num_players + 1 - curr_second
                curr_second = temp
            
            # Want to determine how many players are behind and ahead
            if 2 * curr_second <= num_players + 1:
                num_behind = curr_first - 1
                num_between = curr_second - curr_first - 1
                for i in range(num_behind + 1):
                    for j in range(num_between + 1):
                        min_cand, max_cand = solve(next_round_players, i + 1, i + j + 2)
                        curr_early = min(curr_early, min_cand + 1)
                        curr_late = max(curr_late, max_cand + 1)
            else:
                temp = num_players + 1 - curr_second
                num_behind = curr_first - 1
                num_between = temp - curr_first - 1
                num_ahead = curr_second - temp - 1
                for i in range(num_behind + 1):
                    for j in range(num_between + 1):
                        offset = i + j + 1 + (num_ahead + 1) // 2 + 1
                        min_cand, max_cand = solve(next_round_players, i + 1, offset)
                        curr_early = min(curr_early, min_cand + 1)
                        curr_late = max(curr_late, max_cand + 1)

            return [curr_early, curr_late]
        return solve(n, firstPlayer, secondPlayer)