class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        nums_dict = {}
        num_nums = len(nums)
        for i in range(min(k + 1, num_nums)):
            nums_dict[nums[i]] = nums_dict.get(nums[i], 0) + 1
            if nums_dict[nums[i]] > 1:
                return True

        # Want to move our scope
        for i in range(num_nums - k - 1):
            nums_dict[nums[i]] -= 1
            nums_dict[nums[i + k + 1]] = nums_dict.get(nums[i + k + 1], 0) + 1
            if nums_dict[nums[i + k + 1]] > 1:
                return True
        return False