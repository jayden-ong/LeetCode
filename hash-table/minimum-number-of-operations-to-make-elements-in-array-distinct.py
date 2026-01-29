class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_dict = defaultdict(int)
        num_problems = 0
        for num in nums:
            nums_dict[num] += 1
            if nums_dict[num] == 2:
                num_problems += 1
        
        answer = 0
        curr_index = 0
        while num_problems > 0 and curr_index < len(nums):
            answer += 1
            for i in range(curr_index, min(curr_index + 3, len(nums))):
                nums_dict[nums[i]] -= 1
                if nums_dict[nums[i]] == 1:
                    num_problems -= 1
            curr_index += 3
        return answer
