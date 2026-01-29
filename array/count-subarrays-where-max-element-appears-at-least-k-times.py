class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        num_max_element = 0
        max_element = max(nums)
        right = 0
        answer = 0
        for start in range(len(nums)):
            while right < len(nums) and num_max_element < k:
                if max_element == nums[right]:
                    num_max_element += 1
                right += 1
            
            if num_max_element >= k:
                answer += len(nums) - right + 1
            
            if nums[start] == max_element:
                num_max_element -= 1
            
        return answer