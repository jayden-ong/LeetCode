class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        smallest = min(nums)
        index_smallest = nums.index(smallest)
        # Must be increasing entire time
        prev = smallest
        i = (index_smallest + 1) % len(nums)
        while i != index_smallest:
            if prev >= nums[i]:
                return -1
            prev = nums[i]
            i = (i + 1) % len(nums)
        return (len(nums) - index_smallest) % len(nums)
