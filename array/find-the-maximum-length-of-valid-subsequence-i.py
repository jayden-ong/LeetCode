class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # All even
        #    odd + odd = even and even + even = even
        num_even = 0
        num_odd = 0
        alternate = 1
        is_even = nums[0] % 2 == 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                num_odd += 1
            else:
                num_even += 1
            
            if i > 0:
                if (nums[i] % 2 == 0 and not is_even) or (nums[i] % 2 == 1 and is_even):
                    alternate += 1
                    is_even = not is_even
        return max([num_even, num_odd, alternate])