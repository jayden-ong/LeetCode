class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # We can change three of the elements to be the exact same
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        left = 0
        right = len(nums) - 1
        nums_length = len(nums)
        answers = [nums[nums_length - 4] - nums[0], nums[nums_length - 3] - nums[1], nums[nums_length - 2] - nums[2], nums[nums_length - 1] - nums[3]]
        return min(answers)