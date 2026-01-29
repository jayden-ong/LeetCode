class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
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
        
        starting_point_found = False
        num_cols = len(matrix[0])
        num_rows = len(matrix)
        curr_heights = [0] * num_cols
        best_rectangle = 0
        for row in matrix:
            for j in range(num_cols):
                if row[j] == '0':
                    curr_heights[j] = 0
                else:
                    curr_heights[j] += 1
            best_rectangle = max(best_rectangle, largestRectangleArea(curr_heights))
        return best_rectangle
                    
