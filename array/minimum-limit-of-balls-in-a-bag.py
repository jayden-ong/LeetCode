class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Determine if it is possible to divide bags such that each bag has at most highest_penalty balls
        def possible_penalty(highest_penalty):
            if highest_penalty == 0:
                return False
            
            num_splits = 0
            for num in nums:
                if num > highest_penalty:
                    num_splits += num // highest_penalty
                    if num % highest_penalty == 0:
                        num_splits -= 1 

                if num_splits > maxOperations:
                    return False
            return True
        
        left = 0
        right = max(nums)
        while left < right:
            mid = (left + right) // 2
            if possible_penalty(mid):
                right = mid
            else:
                left = mid + 1

        return left