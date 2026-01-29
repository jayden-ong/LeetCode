class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        modulo_dict = defaultdict(int)
        answer = 0
        curr = 0
        modulo_dict[0] += 1
        for i in range(len(nums)):
            if nums[i] % modulo == k:
                curr += 1
            
            answer += modulo_dict[(curr - k + modulo) % modulo]
            modulo_dict[curr % modulo] += 1
        return answer