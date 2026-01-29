class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        answer = float('inf')
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        answer = min(answer, nums[i] + nums[j] + nums[k])
        if answer == float('inf'):
            return -1
        return answer