class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    answer = max(answer, (nums[i] - nums[j]) * nums[k])
        return answer 