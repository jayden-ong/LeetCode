class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        answer = 0
        curr_answer = 0
        for i in range(len(prices)):
            if k // 2 <= i < k:
                curr_answer += prices[i]
            elif i >= k:
                curr_answer += prices[i] * strategy[i]
            
            answer += prices[i] * strategy[i]
        
        answer = max(answer, curr_answer)
        halfway = k // 2
        for i in range(k, len(prices)):
            # index i becomes a sell no matter what
            if strategy[i] == -1:
                curr_answer += 2 * prices[i]
            elif strategy[i] == 0:
                curr_answer += prices[i]
            
            # index i - k goes back to normal (in our answer it was a hold)
            curr_answer += prices[i - k] * strategy[i - k]

            # the halfway index now becomes part of the first half of consec.
            curr_answer -= prices[halfway]
            halfway += 1
            answer = max(answer, curr_answer)

        return answer