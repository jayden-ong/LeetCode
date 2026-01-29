class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        target = (len(rolls) + n) * mean
        remainder = target - sum(rolls)
        if remainder // n > 6 or remainder // n < 1:
            return []
        answer = [remainder // n] * n
        for i in range(remainder % n):
            answer[i] += 1
            if answer[i] > 6:
                return []
        return answer