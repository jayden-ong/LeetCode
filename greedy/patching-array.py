class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        answer = 0
        curr_max = 0
        for num in nums:
            while curr_max < n and curr_max + 1 < num:
                curr_max = curr_max * 2 + 1
                answer += 1
                
            if curr_max >= n:
                return answer
            
            curr_max += num
        
        while curr_max < n:
            curr_max = curr_max * 2 + 1
            answer += 1
        return answer
        
            
                
            
            
            