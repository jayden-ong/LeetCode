class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        sum_left = [0] * len(nums)
        sum_right = [0] * len(nums)
        curr_left = 0
        curr_right = sum(nums)
        for i, num in enumerate(nums):
            sum_left[i] = curr_left
            sum_right[i] = curr_right
            curr_left += num
            curr_right -= num
        
        answer = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if abs(sum_left[i] - sum_right[i]) == 0:
                    answer += 2
                elif abs(sum_left[i] - sum_right[i]) == 1:
                    answer += 1
        return answer
            