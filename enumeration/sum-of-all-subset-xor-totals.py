from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def XOR(nums):
            answer = 0
            for num in nums:
                answer ^= num
            return answer

        answer = 0
        for i in range(1, len(nums) + 1):
            for combination in list(combinations(nums, i)):
                answer += XOR(combination)
        return answer