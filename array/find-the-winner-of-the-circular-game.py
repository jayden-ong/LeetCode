class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        curr_players = []
        for i in range(n):
            curr_players.append(i + 1)
            
        curr_index = 0
        while len(curr_players) > 1:
            curr_index += k - 1
            curr_index %= len(curr_players)
            curr_players = curr_players[:curr_index] + curr_players[curr_index + 1:]
            curr_index %= len(curr_players)
            
        return curr_players[0]