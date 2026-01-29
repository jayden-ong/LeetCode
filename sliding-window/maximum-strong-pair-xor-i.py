class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    answer = max(answer, nums[i] ^ nums[j])
        return answer