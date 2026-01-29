class Solution:
    def average(self, salary: List[int]) -> float:
        answer = 0
        smallest = float('inf')
        largest = float('-inf')
        divisor = 0
        for money in salary:
            answer += money
            smallest = min(smallest, money)
            largest = max(largest, money)
            divisor += 1
        answer -= (smallest + largest)
        return answer / (divisor - 2)
