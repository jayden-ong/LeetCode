class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        num_nums = len(nums)
        num_divisors = len(divisors)
        answer = None
        highest_divis_score = 0
        for j in range(num_divisors):
            curr_score = 0
            for i in range(num_nums):
                if nums[i] % divisors[j] == 0:
                    curr_score += 1
            
            if answer is None or curr_score > highest_divis_score or (curr_score == highest_divis_score and divisors[j] < answer):
                answer = divisors[j]
                highest_divis_score = curr_score

        return answer