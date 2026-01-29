class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(32):
            curr = 0
            curr_mask = 1 << i
            for num in nums:
                if num & curr_mask != 0:
                    curr += 1
            
            if curr >= k:
                answer += 1 * pow(2, i)
        return answer