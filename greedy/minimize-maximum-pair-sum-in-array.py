class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = float('-inf')
        for i in range(len(nums) // 2):
            answer = max(answer, nums[i] + nums[len(nums) - 1 - i])
        return answer