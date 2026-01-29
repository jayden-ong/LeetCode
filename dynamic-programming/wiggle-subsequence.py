class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1
        
        # Answer is always at least 1
        answer = 1
        i = 1
        # Need to find a starting point where adjacent elements are not equal
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1
        
        if i < len(nums):
            positive_diff = nums[i] > nums[i - 1]
        else:
            return 1
        answer += 1
        for i in range(i + 1, len(nums)):
            # Is wiggle sequence
            if positive_diff and nums[i] < nums[i - 1]:
                answer += 1
                positive_diff = not positive_diff
            elif not positive_diff and nums[i] > nums[i - 1]:
                answer += 1
                positive_diff = not positive_diff
        return answer