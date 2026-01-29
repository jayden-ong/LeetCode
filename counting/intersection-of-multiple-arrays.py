class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        curr_set = set(nums[0])
        num_nums = len(nums)
        for i in range(1, num_nums):
            curr_set = curr_set.intersection(set(nums[i]))
        
        answer = list(curr_set)
        answer.sort()
        return answer