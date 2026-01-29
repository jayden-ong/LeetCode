class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_nums = len(nums)
        answer = 0
        for i in range(1, num_nums):
            if nums[i - 1] >= nums[i]:
                answer += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return answer