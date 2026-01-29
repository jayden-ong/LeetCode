class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        num_children = len(happiness)
        answer = 0
        decreases = 0
        for i in range(num_children - 1, num_children - 1 - k, -1):
            answer += max(0, happiness[i] - decreases)
            decreases += 1
        return answer