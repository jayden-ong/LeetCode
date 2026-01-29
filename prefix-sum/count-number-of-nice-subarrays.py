class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # [0,0,0,1,0,0,1,0,0,0]
        # [0,0,0,1,1,1,2,2,2,2]
        nums_dict = {0 : 1}
        curr = 0
        answer = 0
        for num in nums:
            if num % 2 == 1:
                curr += 1
            
            if curr in nums_dict:
                nums_dict[curr] += 1
            else:
                nums_dict[curr] = 1
            
            if curr >= k:
                answer += nums_dict[curr - k]
        return answer