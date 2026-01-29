class Solution:
    def search(self, nums: List[int], target: int) -> int:
        num_nums = len(nums)
        left = 0
        right = num_nums - 1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target == nums[mid]:
                return mid
            else:
                left = mid + 1
        return -1