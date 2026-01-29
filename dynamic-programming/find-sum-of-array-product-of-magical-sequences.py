from functools import lru_cache
class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        # seq is a list of indices
        # If m and k are the same, all sequences are magical
        # Need to figure out how many permutations there are of size k given a list of length n
        # If m > k, we need m - k duplicates
        # Each sequence has k possible elements that can be duplicated
        #      Need to figure out how many permutations for those k elements exist
        @lru_cache(None)
        def dfs(num_remaining, unique_needed, curr_index, curr_binary):
            if num_remaining < 0 or unique_needed < 0 or num_remaining + curr_binary.bit_count() < unique_needed:
                return 0
            elif num_remaining == 0:
                if unique_needed == curr_binary.bit_count():
                    return 1
                return 0
            elif curr_index >= len(nums):
                return 0
            
            answer = 0
            for i in range(num_remaining + 1):
                num_combs = math.comb(num_remaining, i) * pow(nums[curr_index], i, MOD) % MOD
                new_binary = curr_binary + i
                answer += num_combs * dfs(num_remaining - i, unique_needed - (new_binary % 2), curr_index + 1, new_binary // 2)
                answer %= MOD
            return answer
        
        return dfs(m, k, 0, 0)