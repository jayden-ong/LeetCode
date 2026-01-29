class Solution:
    def totalMoney(self, n: int) -> int:
        # 2,3,4,5,6,7,8
        # first week - 8,8,8,4 second week - 10,10,10,5 third week - 12,12,12,6
        num_weeks = n // 7
        remaining_days = n % 7

        answer = 0
        amount_earned = 8
        for i in range(num_weeks):
            answer += (3 * amount_earned) + (amount_earned // 2)
            amount_earned += 2
        
        amount_earned = num_weeks + 1
        for j in range(remaining_days):
            answer += amount_earned
            amount_earned += 1
        return answer