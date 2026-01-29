class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        array_remainder = sum(nums) % p
        if array_remainder == 0:
            return 0
        
        curr_sum = 0
        answers_dict = {0 : -1}
        answer = len(nums)
        for i in range(len(nums)):
            curr_sum += nums[i]
            curr_remainder = curr_sum % p
            # We want our remainder to be array_remainder, so we know the sum of the rest is divisible by p
            # The desired_remainder formula tells us which remainder we need to find
            # If we can find it, we can get rid of everything in between and get the desired remainder
            desired_remainder = (curr_remainder - array_remainder + p) % p
            if desired_remainder in answers_dict:
                answer = min(answer, i - answers_dict[desired_remainder])
            answers_dict[curr_remainder] = i
        if answer == len(nums):
            return -1
        return answer
