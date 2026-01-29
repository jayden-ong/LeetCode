class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        num_unique = len(set(nums))
        right = 0
        nums_dict = defaultdict(int)
        curr = 0
        answer = 0
        for left in range(len(nums)):
            while right < len(nums) and curr < num_unique:
                nums_dict[nums[right]] += 1
                if nums_dict[nums[right]] == 1:
                    curr += 1
                right += 1
            
            if num_unique == curr:
                answer += len(nums) - right + 1
            
            nums_dict[nums[left]] -= 1
            if nums_dict[nums[left]] == 0:
                curr -= 1
            
        return answer
            
