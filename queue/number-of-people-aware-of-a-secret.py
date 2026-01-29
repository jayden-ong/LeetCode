class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        # Index 0 is for how many people can spread, Index 1 is for how many people forget
        schedule = [[0, 0] for i in range(n + 1)]
        if 1 + delay <= n:
            schedule[1 + delay][0] = 1
        if 1 + forget <= n:
            schedule[1 + forget][1] = 1

        answer = 1
        can_spread = 0
        for i in range(1, n + 1):
            can_spread = can_spread + schedule[i][0] - schedule[i][1]
            if i + delay <= n:
                schedule[i + delay][0] += can_spread
            if i + forget <= n:
                schedule[i + forget][1] += can_spread
            answer = answer + can_spread - schedule[i][1]
        return answer % MOD