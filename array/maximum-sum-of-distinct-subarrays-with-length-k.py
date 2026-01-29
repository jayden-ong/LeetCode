class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        curr_sum = 0
        nums_dict = {}
        num_violations = 0
        for i in range(k):
            if nums[i] in nums_dict:
                num_violations += 1
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1
            curr_sum += nums[i]
        
        if num_violations == 0:
            answer = max(answer, curr_sum)

        for i in range(k, len(nums)):
            # Remove first element from dict
            first_element = nums[i - k]
            curr_sum -= first_element
            nums_dict[first_element] -= 1
            if nums_dict[first_element] >= 1:
                num_violations -= 1
            
            next_element = nums[i]
            if next_element not in nums_dict or nums_dict[next_element] == 0:
                nums_dict[next_element] = 1
            else:
                nums_dict[next_element] += 1
                num_violations += 1
            curr_sum += next_element
            
            if num_violations == 0:
                answer = max(answer, curr_sum)
        return answer