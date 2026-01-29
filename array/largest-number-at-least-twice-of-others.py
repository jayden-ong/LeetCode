class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = None
        next_largest = None
        ind = -1
        for i in range(len(nums)):
            if largest is None:
                largest = nums[i]
                ind = i
            else:
                if nums[i] > largest:
                    next_largest = largest
                    largest = nums[i]
                    ind = i
                elif nums[i] < largest and (next_largest is None or nums[i] > next_largest):
                    next_largest = nums[i]
        if largest >= 2 * next_largest:
            return ind
        return -1