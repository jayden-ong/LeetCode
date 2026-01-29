class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # 0 is undecided, 1 is monotonic decreasing and 2 is monotonic decreasing
        monotonic = 0
        num_nums = len(nums)
        for i in range(1, num_nums):
            # decreasing
            if nums[i - 1] > nums[i]:
                if monotonic == 0:
                    monotonic = 1
                elif monotonic == 2:
                    return False
            # increasing
            elif nums[i - 1] < nums[i]:
                if monotonic == 0:
                    monotonic = 2
                elif monotonic == 1:
                    return False

        return True