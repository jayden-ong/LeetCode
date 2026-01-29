class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        # We want to decrease the amount of unnecessary comparisons
        for i in range(len(nums)):
            if stack == [] or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        answer = 0
        for i in range(len(nums) - 1, -1 ,-1):
            # The top of the stack contains indices such that their values in nums decrease
            # We want the latest smallest number
            # If we can make a ramp, no point in doing the rest of the comparisons as they lead to worse results
            while stack and nums[stack[-1]] <= nums[i]:
                answer = max(answer, i - stack[-1])
                stack.pop()
        return answer