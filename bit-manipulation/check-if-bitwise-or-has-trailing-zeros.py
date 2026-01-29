class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        num_even = 0
        for num in nums:
            if num % 2 == 0:
                num_even += 1

            if num_even >= 2:
                return True
        return False