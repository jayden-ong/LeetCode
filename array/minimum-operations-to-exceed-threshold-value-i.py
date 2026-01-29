class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        for num in nums:
            if num < k:
                answer += 1
        return answer