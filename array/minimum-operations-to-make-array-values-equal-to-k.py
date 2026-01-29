class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        
        answer_set = set()
        for num in nums:
            if num > k:
                answer_set.add(num)
        return len(answer_set)