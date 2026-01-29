class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        streak = 0
        answer = 0
        # Want to keep track of the index of the furthest number making subarray valid
        i = 0
        furthest_valid = None
        for num in nums:
            if left <= num <= right:
                streak += 1
                answer += streak
                furthest_valid = i
            elif num < left:
                streak += 1
                if furthest_valid is not None:
                    answer += (streak) - (i - furthest_valid)
            else:
                streak = 0
                furthest_valid = None
            i += 1
        return answer