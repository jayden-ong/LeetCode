class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        window_dict = defaultdict(int)
        left, right = 0, 0
        answer = 0
        for i in range(nums[0], nums[-1] + 1):
            while right < len(nums) and nums[right] <= i + k:
                window_dict[nums[right]] += 1
                right += 1
            
            while left < len(nums) and nums[left] < i - k:
                window_dict[nums[left]] -= 1
                left += 1
            
            answer = max(answer, min(right - left, window_dict[i] + numOperations))

        return answer
