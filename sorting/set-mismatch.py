class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_nums = len(nums)
        curr_sum = 0
        curr_nums_sum = 0
        nums_dict = {}
        for i in range(num_nums):
            curr_nums_sum += nums[i]
            curr_sum += i + 1
            if nums[i] in nums_dict:
                duplicate = nums[i]
            else:
                nums_dict[nums[i]] = True
        
        return [duplicate, curr_sum - (curr_nums_sum - duplicate)]
        