class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        num_nums = len(nums)
        sum_set = set()
        for i in range(num_nums - 1):
            if nums[i] + nums[i + 1] in sum_set:
                return True
            else:
                sum_set.add(nums[i] + nums[i + 1])
        return False