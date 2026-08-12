class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        right = 0
        answer = 1
        curr_freq = defaultdict(int)
        violation = False
        for i in range(len(nums)):
            while right < len(nums) and not violation:
                curr_freq[nums[right]] += 1
                if curr_freq[nums[right]] > k:
                    violation = True
                right += 1

            answer = max(answer, right - i - 1)
            
            curr_freq[nums[i]] -= 1
            if curr_freq[nums[i]] == k:
                violation = False
        return answer