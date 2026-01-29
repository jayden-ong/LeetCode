class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        # Store smallest element to the left 
        smallest_left = []
        curr_smallest = float('inf')
        for num in nums:
            smallest_left.append(curr_smallest)
            curr_smallest = min(curr_smallest, num)
        
        stack = [nums[-1]]
        for i in range(len(nums) - 2, 0, -1):
            # Check if the current index is a potential "3" candidate
            if nums[i] > smallest_left[i]:
                # Next, check if the top of the stack is a potential "2" candidate                
                # Cannot be a "2"
                while stack and stack[-1] <= smallest_left[i]:
                    stack.pop()
                
                if stack and smallest_left[i] < stack[-1] < nums[i]:
                    return True
                
                stack.append(nums[i])
        return False