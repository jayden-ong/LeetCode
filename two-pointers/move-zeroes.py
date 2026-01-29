class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Keep track of all indices of 0
        non_zero_indices = []
        num_nums = 0
        num_non_zero = 0
        # Only want to move non_zero if it is seen after a zero
        zero_seen = False
        for num in nums:
            if num != 0 and zero_seen:
                non_zero_indices.append(num_nums)
                num_non_zero += 1
            
            if num == 0:
                zero_seen = True
            
            num_nums += 1
        
        curr_non_zero_index = 0
        i = 0
        while curr_non_zero_index < num_non_zero:
            if nums[i] == 0:
                nums[i] = nums[non_zero_indices[curr_non_zero_index]]
                nums[non_zero_indices[curr_non_zero_index]] = 0
                curr_non_zero_index += 1
            i += 1
