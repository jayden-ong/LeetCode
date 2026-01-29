class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        answer = 0
        sum_nums = 0
        for i in range(len(nums)):
            answer += nums[i] * i
            sum_nums += nums[i]
        
        prev = answer
        curr_ind = len(nums) - 1
        for i in range(1, len(nums)):
            prev += sum_nums
            prev -= (nums[curr_ind] * len(nums))
            curr_ind -= 1
            answer = max(answer, prev)
        return answer