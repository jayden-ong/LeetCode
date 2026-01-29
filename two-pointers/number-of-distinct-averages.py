class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        averages_set = set()
        nums.sort()
        left = 0
        right = len(nums) - 1
        answer = 0
        while left < right:
            average = (nums[left] + nums[right]) / 2
            if average not in averages_set:
                answer += 1
                averages_set.add(average)
            left += 1
            right -= 1
        return answer
