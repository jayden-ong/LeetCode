class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        amount = 0
        for i in range(len(nums) + 1):
            amount += i
        
        for num in nums:
            amount -= num
        
        return amount