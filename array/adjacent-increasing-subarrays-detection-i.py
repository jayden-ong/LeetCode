class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def check_increasing(nums):
            for i in range(len(nums) - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        
        for i in range(len(nums) - 2 * k + 1):
            if check_increasing(nums[i:i + k]) and check_increasing(nums[i + k:i + 2 * k]):
                return True

        return False