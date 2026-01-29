class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_nums = len(nums)
        def find_last_point_of_decrease():
            for i in range(num_nums - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    return i
            return -1
        
        def find_smallest(index, lower):
            index_of_smallest = -1
            smallest = float('inf')
            for i in range(index, num_nums):
                if nums[i] > lower and nums[i] <= smallest:
                    smallest = nums[i]
                    index_of_smallest = i
            return index_of_smallest

        # If it's decreasing, we are at the end
        # If it's increasing, we are at the beginning - swap last two numbers
        # If it's decreasing at some point, we want to know when the last point of decrease is
        # Need to find the number that is s
        # [1,2,3,5,4] -> [1,2,4,5,3]
        # [1,2,7,6,5,4,3]
        # [1,2,3,5,4,3,7,6]
        # [1,2,3,4,4,4]
        # Want to swap with smallest one that is greater, then by earliest
        # [1,2,3,4,4,4,6,11,11,9]
        # [7,4,9,6,5,3,2,1]
        # [7,5,9,6,4,3,2,1]

        if num_nums == 1:
            return
        # Check last two to see if increasing
        elif num_nums == 2 or nums[-2] < nums[-1]:
            temp = nums[-1]
            nums[-1] = nums[-2]
            nums[-2] = temp
            return 
        else:
            point_of_decrease = find_last_point_of_decrease()
            # If it is -1, the entire thing is decreasing
            # If it is 0, it increases between 0 and 1, then decreases
            first_swapping_point = point_of_decrease + 1
            last_swapping_point = num_nums - 1
            if point_of_decrease > -1:
                swapping_index = find_smallest(point_of_decrease + 1, nums[point_of_decrease])
                temp = nums[point_of_decrease]
                nums[point_of_decrease] = nums[swapping_index]
                nums[swapping_index] = temp

            while first_swapping_point < last_swapping_point:
                temp = nums[first_swapping_point]
                nums[first_swapping_point] = nums[last_swapping_point]
                nums[last_swapping_point] = temp
                first_swapping_point += 1
                last_swapping_point -= 1
            return 