class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        length_nums = len(nums)
        for i in range(length_nums - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        non_zeros = []
        zeros = []
        for num in nums:
            if num == 0:
                zeros.append(0)
            else:
                non_zeros.append(num)
        
        return non_zeros + zeros