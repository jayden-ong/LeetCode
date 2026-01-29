class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Will have two pointers
        # The first one will represent which element we are replacing
        # The second one will represent which element we are looking at
        # Will return that first pointer subtracted by 1
        curr_streak = 1
        num_nums = len(nums)
        first_pointer = 1
        second_pointer = 1
        while second_pointer < num_nums:
            if nums[second_pointer] == nums[second_pointer - 1]:
                curr_streak += 1
                if curr_streak > 2:
                    # Once we see a third of the same, we start looking at
                    # nums in advance. Once we see something different, that
                    # is what we replace
                    old_val = nums[second_pointer]
                    while second_pointer < num_nums and nums[second_pointer] == old_val:
                        second_pointer += 1
                    
                    if second_pointer >= num_nums:
                        return first_pointer
                    
                    nums[first_pointer] = nums[second_pointer]
                    curr_streak = 1
                else:
                    nums[first_pointer] = nums[second_pointer]
            else:
                curr_streak = 1
                nums[first_pointer] = nums[second_pointer]
            second_pointer += 1
            first_pointer += 1
        # Look at later
        return first_pointer