class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        if right == -1:
            return [-1, -1]
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                break

        if left > right:
            return [-1, -1]
        
        # The beginning and ending bounds of the target must be between left and mid and right and mid
        upper_bound = mid
        # upper_bound = 3, left = 3, new_mid = 3, nums[new_mid] = 8, target = 8
        while nums[left] != target:
            new_mid = (left + upper_bound) // 2
            # Cannot be greater since it is sorted
            if nums[new_mid] < target:
                left = new_mid + 1
            else:
                # Must be equal
                upper_bound = new_mid
                
        lower_bound = mid
        while nums[right] != target:
            new_mid = (lower_bound + right) // 2
            # Cannot be less since it is sorted
            if nums[new_mid] > target:
                right = new_mid - 1
            else:
                # Must be equal
                lower_bound = new_mid
                if right - lower_bound == 1:
                    right = lower_bound
                    break

        return [left, right]