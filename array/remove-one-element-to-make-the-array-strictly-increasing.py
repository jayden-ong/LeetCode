class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        num_nums = len(nums)
        num_fails = 0
        for i in range(num_nums - 1):
            if nums[i] >= nums[i + 1]:
                if num_fails > 0:
                    return False
                else:
                    num_fails += 1
                    if (i > 0 and nums[i - 1] >= nums[i + 1]) and (i < num_nums - 2 and nums[i] >= nums[i + 2]):
                        return False        
        return True