class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        answer = 0
        for i in range(32):
            num_zero = 0
            num_one = 0
            for num in nums:
                curr_mask = 1 << i
                if curr_mask & num:
                    num_one += 1
                else:
                    num_zero += 1
            answer += num_zero * num_one
        return answer