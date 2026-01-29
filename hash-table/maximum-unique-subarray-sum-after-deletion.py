class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums_set = set(nums)
        answer = 0
        smallest_neg = float('-inf')
        nums_added = 0
        for num in nums_set:
            if num < 0:
                smallest_neg = max(smallest_neg, num)
            
            if num >= 0:
                answer += num
                nums_added += 1
        if nums_added == 0:
            return smallest_neg
        return answer