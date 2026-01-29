class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        integer_set = set()
        for num in nums:
            for i in range(num[0], num[1] + 1):
                integer_set.add(i)
        return len(integer_set)