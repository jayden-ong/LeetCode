class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # If there is at least one 1, we can spread 1 to every entry
        # It is impossible if all nums have a common divisor greater than 1
        num_ones = 0
        curr_gcd = 0
        for num in nums:
            if num == 1:
                num_ones += 1
            curr_gcd = gcd(curr_gcd, num)
        
        if num_ones > 0:
            return len(nums) - num_ones
        
        # The smallest num we can reduce the array to is curr_gcd
        if curr_gcd > 1:
            return -1
        
        # Want to create a 1 as quickly as possible
        smallest_required = len(nums)
        for i in range(len(nums)):
            curr_gcd = 0
            for j in range(i, len(nums)):
                curr_gcd = gcd(curr_gcd, nums[j])
                if curr_gcd == 1:
                    smallest_required = min(smallest_required, j - i + 1)
                    break
        return smallest_required + len(nums) - 2