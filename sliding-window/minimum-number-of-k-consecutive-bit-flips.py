from collections import deque
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        answer = 0
        stack = deque()
        for i in range(len(nums) - k + 1):
            if (nums[i] == 0 and len(stack) % 2 == 0) or (nums[i] == 1 and len(stack) % 2 == 1):
                answer += 1
                stack.append(i + k - 1)
            
            # Stack will hold the indices involved in flips
            if stack and stack[0] == i:
                stack.popleft() 

        for i in range(len(nums) - k + 1, len(nums)):
            if (nums[i] == 0 and len(stack) % 2 == 0) or (nums[i] == 1 and len(stack) % 2 == 1):
                return -1
            
            # Stack will hold the indices involved in flips
            if stack and stack[0] == i:
                stack.popleft()

        
        return answer