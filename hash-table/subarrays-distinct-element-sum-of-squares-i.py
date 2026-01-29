class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        answer = 0
        for i in range(1, len(nums) + 1):
            for j in range(len(nums) - i + 1):
                answer += pow(len(set(nums[j:j + i])), 2)
        return answer