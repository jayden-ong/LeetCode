class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        
        nums.sort()
        def validate_threshold(threshold):
            i = 0
            num_valid = 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i + 1]) <= threshold:
                    i += 2
                    num_valid += 1
                else:
                    i += 1
                
                if num_valid == p:
                    return True
            return False
        # Can we make our answer less than a certain threshold
        left = 0
        right = abs(nums[0] - nums[-1])
        while left < right:
            mid = (left + right) // 2
            if validate_threshold(mid):
                right = mid
            else:
                left = mid + 1
        return left

