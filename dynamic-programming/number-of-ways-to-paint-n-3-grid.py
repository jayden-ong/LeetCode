class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        pattern_one, pattern_two = 6, 6
        for i in range(2, n + 1):
            new_pattern_one, new_pattern_two = (3 * pattern_one + 2 * pattern_two) % MOD, (2 * pattern_one + 2 * pattern_two) % MOD
            pattern_one, pattern_two = new_pattern_one, new_pattern_two
        
        return (pattern_one + pattern_two) % MOD