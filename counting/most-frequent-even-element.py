class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        answer = -1
        answer_freq = 1
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if nums[i] in nums_dict:
                    nums_dict[nums[i]] += 1
                else:
                    nums_dict[nums[i]] = 1
                
                if answer == -1 or nums_dict[nums[i]] > answer_freq or (nums_dict[nums[i]] == answer_freq and nums[i] < answer):
                    answer = nums[i]
                
                answer_freq = nums_dict[answer]
        return answer
                