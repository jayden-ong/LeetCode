class Solution:
    def arraySign(self, nums: List[int]) -> int:
        num_negatives = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                num_negatives += 1
        
        if num_negatives % 2 == 0:
            return 1
        return -1