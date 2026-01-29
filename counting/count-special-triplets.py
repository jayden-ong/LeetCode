class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        total_nums = defaultdict(int)
        for num in nums:
            total_nums[num] += 1
        
        answer = 0
        curr_count = defaultdict(int)
        for num in nums:
            target = num * 2
            if num == 0:
                answer = (answer + curr_count[target] * (total_nums[target] - curr_count[target] - 1)) % MOD
            else:
                answer = (answer + curr_count[target] * (total_nums[target] - curr_count[target])) % MOD
            curr_count[num] += 1
        return answer