class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        num_mod = 1
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if num_mod <= 0:
                    return False
                else:
                    # Either have to change nums[i - 1] or nums[i]
                    if (i - 2 >= 0 and nums[i - 2] > nums[i]) and (i + 1 < len(nums) and nums[i - 1] > nums[i + 1]):
                        return False
                    num_mod -= 1
        return True
