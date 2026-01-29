class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        answer = 0
        curr_sum = 0
        for i in range(1, n + 1):
            if i not in banned_set and i + curr_sum <= maxSum:
                answer += 1
                curr_sum += i
            
            if i + curr_sum > maxSum:
                return answer
        return answer