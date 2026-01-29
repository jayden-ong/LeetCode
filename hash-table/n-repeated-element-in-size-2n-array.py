class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                return num
            else:
                nums_dict[num] = True
                