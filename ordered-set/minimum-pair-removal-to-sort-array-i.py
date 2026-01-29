class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def check_non_decreasing(curr_nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        
        answer = 0
        while not check_non_decreasing(nums):
            curr_index, curr_min = 0, float('inf')
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < curr_min:
                    curr_index, curr_min = i, nums[i] + nums[i + 1]
            
            if curr_index + 2 >= len(nums):
                nums = nums[:curr_index] + [curr_min]
            else:
                nums = nums[:curr_index] + [curr_min] + nums[curr_index + 2:]
            answer += 1
        return answer
            