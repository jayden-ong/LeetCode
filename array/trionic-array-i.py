class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        increasing_one = decreasing_one = increasing_two = False
        point = None
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return False
            elif nums[i] < nums[i + 1]:
                if increasing_one:
                    decreasing_one = True
                    point = i
                    break
            else:
                if not increasing_one and i == 0:
                    return False
                increasing_one = True
        
        if point is None:
            return False
        
        for i in range(point, len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True
