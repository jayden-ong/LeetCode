class Solution:
    def isGood(self, nums: List[int]) -> bool:
        num_nums = len(nums)
        highest = max(nums)
        num_highest = 0
        nums_set = set()
        for num in nums:
            if num == highest:
                num_highest += 1
            else:
                if num not in nums_set:
                    nums_set.add(num)
                else:
                    return False
        return num_highest == 2 and len(nums_set) == num_nums - 2 and len(nums) == highest + 1