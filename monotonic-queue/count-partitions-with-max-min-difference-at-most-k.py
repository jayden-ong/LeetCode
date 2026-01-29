class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        # How many ways are there to partition i:?
        MOD = pow(10, 9) + 7
        dp = [0] * (len(nums) + 1)
        dp[0] = 1
        prefix = [0] * (len(nums) + 1)
        prefix[0] = 1
        curr_nums = SortedList()

        left = 0
        for i in range(len(nums)):
            curr_nums.add(nums[i])
            while left <= i and curr_nums[-1] - curr_nums[0] > k:
                curr_nums.remove(nums[left])
                left += 1
            
            dp[i + 1] = prefix[i] % MOD
            if left > 0:
                dp[i + 1] = (dp[i + 1] - prefix[left - 1]) % MOD
            prefix[i + 1] = (prefix[i] + dp[i + 1] % MOD)
            
        return dp[len(nums)]
