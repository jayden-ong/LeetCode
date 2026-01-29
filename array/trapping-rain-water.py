class Solution:
    def trap(self, height: List[int]) -> int:
        # first and last spaces cannot trap any rainwater as there is no wall to the left and right
        num_heights = 0
        tallest_wall = -1
        tallest_wall_index = -1
        for wall in height:
            num_heights += 1
            if tallest_wall < wall:
                tallest_wall = wall
                tallest_wall_index = num_heights - 1
        
        curr_water = 0
        tallest_left = -1
        for i in range(1, tallest_wall_index):
            # Want to update tallest left wall
            if height[i - 1] > tallest_left:
                tallest_left = height[i - 1]
            
            max_capacity = min(tallest_left, tallest_wall)
            if max_capacity > height[i]:
                curr_water += max_capacity - height[i]
        
        tallest_right = -1
        for i in range(num_heights - 2, tallest_wall_index, -1):
            if height[i + 1] > tallest_right:
                tallest_right = height[i + 1]
            
            max_capacity = min(tallest_wall, tallest_right)
            if max_capacity > height[i]:
                curr_water += max_capacity - height[i]
        
        return curr_water