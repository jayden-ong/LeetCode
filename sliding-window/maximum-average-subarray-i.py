class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        num_nums = len(nums)
        max_sum = 0
        for i in range(k):
            max_sum += nums[i]
        
        curr_sum = max_sum
        for i in range(1, num_nums - k + 1):
            curr_sum -= nums[i - 1]
            curr_sum += nums[i + k - 1]
            max_sum = max(curr_sum, max_sum)
        return max_sum/k
        