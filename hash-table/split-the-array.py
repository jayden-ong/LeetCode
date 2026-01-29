class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
            
            if nums_dict[num] > 2:
                return False

        return len(set_nums) >= len(nums) // 2