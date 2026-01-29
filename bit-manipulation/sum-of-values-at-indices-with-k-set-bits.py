class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(len(nums)):
            if i.bit_count() == k:
                answer += nums[i]
        return answer