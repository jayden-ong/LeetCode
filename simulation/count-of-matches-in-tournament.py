class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams_remaining = n
        num_matches = 0
        while teams_remaining > 1:
            num_matches += (teams_remaining // 2)
            leftover = teams_remaining % 2
            teams_remaining //= 2
            teams_remaining += leftover
        return num_matches