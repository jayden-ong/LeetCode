class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        curr_bottleneck = []
        num_heights = len(heights)
        starting_left = [0] * num_heights
        starting_right = [num_heights - 1] * num_heights

        for i in range(num_heights):
            if curr_bottleneck != []:
                while curr_bottleneck != [] and heights[curr_bottleneck[-1]] >= heights[i]:
                    curr_bottleneck.pop()
                
                if curr_bottleneck != []:
                    starting_left[i] = curr_bottleneck[-1] + 1
            
            curr_bottleneck.append(i)
        
        curr_bottleneck = []
        for i in range(num_heights - 1, -1, -1):
            if curr_bottleneck != []:
                while curr_bottleneck != [] and heights[curr_bottleneck[-1]] >= heights[i]:
                    curr_bottleneck.pop()
                
                if curr_bottleneck != []:
                    starting_right[i] = curr_bottleneck[-1] - 1
            
            curr_bottleneck.append(i)
        
        curr = -1
        for i in range(num_heights):
            curr = max(curr, (starting_right[i] - starting_left[i] + 1) * heights[i])
        
        return curr
