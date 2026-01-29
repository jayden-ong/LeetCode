class Solution:
    def maxArea(self, height: List[int]) -> int:
        num_heights = len(height)
        left = [0] * num_heights
        right = [num_heights - 1] * num_heights
        # Want the height that is furthest and at least as tall
        for i in range(1, num_heights):
            # The tallest is the bottleneck
            for j in range(i + 1):
                if height[j] >= height[i]:
                    left[i] = j
                    break
                
        
        for i in range(num_heights - 2, -1, -1):
            for j in range(num_heights - 1, i - 1, -1):
                if height[j] >= height[i]:
                    right[i] = j
                    break
            
        curr = -1
        for i in range(num_heights):
            curr = max(curr, (right[i] - left[i]) * height[i])
        return curr
                    