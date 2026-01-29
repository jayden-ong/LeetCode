class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        original_nums = nums.copy()
        nums.sort()
        remaining_sum = sum(nums)
        answer = []
        curr_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            curr_sum += nums[i]
            remaining_sum -= nums[i]
            answer.append(nums[i])
            
            if curr_sum > remaining_sum:
                answer.sort(reverse=True)
                return answer
        answer.sort(reverse=True)
        return answer