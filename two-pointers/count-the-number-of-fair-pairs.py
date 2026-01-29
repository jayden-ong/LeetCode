class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        def get_pairs_less_num(num):
            answer = 0
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < num:
                    # All combinations with left and everything after it will be less than num
                    answer += right - left
                    left += 1
                else:
                    right -= 1
            return answer
        
        return get_pairs_less_num(upper + 1) - get_pairs_less_num(lower)
        