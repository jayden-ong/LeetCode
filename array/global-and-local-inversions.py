class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # All local inversion are also global inversions
        # If there is an i and j where nums[i] > nums[j] and j >= i + 2, return False
        # If the value is greater than the index, there must be at least one local inversion
        for i in range(len(nums)):
            if nums[i] >= i + 2:
                return False
            elif nums[i] == i + 1:
                if nums[i + 1] > nums[i]:
                    return False
        return True
            