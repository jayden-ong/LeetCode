class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        curr = [0] * len(nums)
        for left, right in queries:
            curr[left] -= 1
            if right + 1 < len(nums):
                curr[right + 1] += 1
        
        temp = 0
        for i, num in enumerate(nums):
            temp += curr[i]
            if num + temp > 0:
                return False
        return True