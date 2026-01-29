class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_dict = {}
        high_freq = 0
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
            high_freq = max(high_freq, nums_dict[num])
        
        answer = 0
        for num in nums_dict:
            if nums_dict[num] == high_freq:
                answer += high_freq
        return answer