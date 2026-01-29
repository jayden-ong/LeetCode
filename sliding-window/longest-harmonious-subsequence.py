class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        curr_max = 0
        for num in nums_dict:
            if num + 1 in nums_dict:
                curr_max = max(curr_max, nums_dict[num] + nums_dict[num + 1])
        return curr_max