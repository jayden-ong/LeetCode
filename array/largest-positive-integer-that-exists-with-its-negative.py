class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        items_set = set()
        curr_greatest = -1
        for num in nums:
            if -num in items_set:
                curr_greatest = max(abs(num), curr_greatest)
            items_set.add(num)
        return curr_greatest