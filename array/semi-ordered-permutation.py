class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        smallest = float('inf')
        smallest_index = 0
        largest = float('-inf')
        largest_index = 0
        i = 0
        for num in nums:
            if num < smallest:
                smallest = num
                smallest_index = i
            
            if num > largest:
                largest = num
                largest_index = i
            i += 1
        
        if largest_index > smallest_index:
            return smallest_index + len(nums) - 1 - largest_index
        return smallest_index + len(nums) - largest_index - 2
