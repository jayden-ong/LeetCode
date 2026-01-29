class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        right_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum -= nums[i]
            answer.append(abs(left_sum - right_sum))
            left_sum += nums[i]
        return answer