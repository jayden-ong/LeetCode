class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Want to find the index of the reset
        num_nums = len(nums)
        def find_reset():
            for i in range(1, num_nums):
                if nums[i - 1] > nums[i]:
                    return i
            return 0
        
        # We need to find the reset point and start searching from there
        if target < nums[0]:
            starting_point = find_reset()
            for i in range(starting_point, num_nums):
                if target < nums[i]:
                    return -1
                elif target == nums[i]:
                    return i
            return -1
        elif target > nums[0]:
            last_index = find_reset()
            if last_index == 0:
                last_index = num_nums
            for i in range(last_index):
                if target < nums[i]:
                    return -1
                elif target == nums[i]:
                    return i
            return -1
        return 0