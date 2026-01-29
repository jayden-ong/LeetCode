class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        num_ones = 0
        # Want to determine number of ones
        for num in nums:
            if num == 1:
                num_ones += 1
        
        curr = 0
        for i in range(num_ones):
            if nums[i] == 1:
                curr += 1
        
        next_index = num_ones
        answer = num_ones - curr
        new_nums = nums + nums
        for i in range(len(nums)):
            if new_nums[i] == 1:
                curr -= 1
            
            if new_nums[next_index] == 1:
                curr += 1
            
            answer = min(answer, num_ones - curr)
            next_index += 1
        return answer
