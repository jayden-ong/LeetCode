class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = []
        max_pos_sum = 0
        min_neg_sum = 0
        answer = 0
        curr = 0
        for num in nums:
            curr += num
            max_pos_sum = max(max_pos_sum, curr)
            min_neg_sum = min(min_neg_sum, curr)
            if curr >= 0:
                answer = max(answer, max(curr, curr - min_neg_sum))
            else:
                answer = max(answer, max(abs(curr), abs(curr - max_pos_sum)))
        return answer