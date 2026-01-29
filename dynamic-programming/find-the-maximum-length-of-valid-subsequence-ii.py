class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(k):
            dp = defaultdict(int)
            for j, num in enumerate(nums):
                num %= k
                # Want to know how much "remainder" num will add
                # num = 2, i = 1, k = 3
                remainder_added = (i - num + k) % k
                dp[num] = dp[remainder_added] + 1
                answer = max(answer, dp[num])
        return answer