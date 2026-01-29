class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        right = 0
        nums_dict = defaultdict(int)
        num_pairs = 0
        answer = 0
        for left in range(len(nums)):
            while right < len(nums) and num_pairs < k:
                nums_dict[nums[right]] += 1
                if nums_dict[nums[right]] >= 2:
                    num_pairs += nums_dict[nums[right]] - 1
                right += 1
            if num_pairs < k:
                return answer
            
            answer += len(nums) - right + 1
            nums_dict[nums[left]] -= 1
            if nums_dict[nums[left]] >= 1:
                num_pairs -= nums_dict[nums[left]]
        return answer