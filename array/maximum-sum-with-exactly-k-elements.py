class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        answer = 0
        current_max = max(nums)
        for i in range(k):
            answer += current_max
            current_max += 1
        return answer
