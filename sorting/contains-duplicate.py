class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers_seen = {}
        for num in nums:
            if num in numbers_seen:
                return True
            else:
                numbers_seen[num] = True
        
        return False