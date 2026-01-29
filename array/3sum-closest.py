class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_guess = None
        nums.sort()
        num_nums = len(nums)
        for i in range(num_nums - 2):
            j = i + 1
            k = num_nums - 1
            while j < k:
                guess = nums[i] + nums[j] + nums[k]
                if not closest_guess or abs(guess - target) < abs(closest_guess - target):
                    closest_guess = guess
                
                # Might not have to check to make sure the numbers aren't the same
                if guess == target:
                    return guess
                elif guess < target:
                    j += 1
                else:
                    k -= 1
        return closest_guess