class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # First check if sorted
        is_sorted = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                is_sorted = False
        
        if is_sorted:
            return True

        curr_num_bits = nums[0].bit_count()
        curr_largest = nums[0]
        prev_seg_largest = None
        curr_smallest = nums[0]
        for i in range(1, len(nums) + 1):
            if i != len(nums) and nums[i].bit_count() == curr_num_bits:
                curr_largest = max(curr_largest, nums[i])
                curr_smallest = min(curr_smallest, nums[i])
            else:
                if prev_seg_largest is not None:
                    if curr_smallest <= prev_seg_largest:
                        return False
                
                if i != len(nums):
                    prev_seg_largest = curr_largest
                    curr_largest = nums[i]
                    curr_smallest = nums[i]
                    curr_num_bits = curr_smallest.bit_count()
        return True
                