class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            curr_ind = (l + r) // 2
            if target < nums[curr_ind]:
                r = curr_ind - 1
            elif target == nums[curr_ind]:
                return curr_ind
            elif target > nums[curr_ind]:
                l = curr_ind + 1
        return l