class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # Either remove from one end, remove from both, remove from other
        largest_int, largest_int_pos = float('-inf'), None
        smallest_int, smallest_int_pos = float('inf'), None
        for i, num in enumerate(nums):
            if num > largest_int:
                largest_int, largest_int_pos = num, i
            
            if num < smallest_int:
                smallest_int, smallest_int_pos = num, i
        
        return min([max(largest_int_pos, smallest_int_pos) + 1, max(len(nums) - largest_int_pos, len(nums) - smallest_int_pos), min(largest_int_pos, smallest_int_pos) + 1 + min(len(nums) - largest_int_pos, len(nums) - smallest_int_pos)])