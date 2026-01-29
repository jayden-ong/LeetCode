class Solution:
    def averageValue(self, nums: List[int]) -> int:
        answer = 0
        num_even = 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                answer += num
                num_even += 1
        if num_even == 0:
            return 0
        return answer // num_even