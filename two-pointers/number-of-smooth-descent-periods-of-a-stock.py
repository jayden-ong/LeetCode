class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # length * (length + 1) // 2
        answer = 0
        curr_streak = 1
        for i in range(1, len(prices) + 1):
            if i < len(prices) and prices[i - 1] - 1 == prices[i]:
                curr_streak += 1
            else:
                answer += (curr_streak * (curr_streak + 1)) // 2
                curr_streak = 1

        return answer