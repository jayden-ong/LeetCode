class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # The maximum bitwise OR is the bitwise OR of the entire list
        goal = 0
        for num in nums:
            goal |= num
        
        answer = [0]

        def backtrack(curr_index, curr_val):            
            # Only check at the end
            if curr_index == len(nums):
                if curr_val == goal:
                    answer[0] += 1
                return
            
            backtrack(curr_index + 1, curr_val | nums[curr_index])
            backtrack(curr_index + 1, curr_val)
        
        backtrack(0, 0)
        return answer[0]
