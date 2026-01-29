class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        num_nums = len(nums)
        # If a subset is not beautiful, no superset of it will be beautiful either
        def recursive(curr_index, curr_set):
            answer = 0
            if curr_index >= num_nums:
                return answer
            # There are two options:
            # Do not add to set
            set_copy = curr_set.copy()
            answer += recursive(curr_index + 1, set_copy)
            # Add to set
            if nums[curr_index] - k not in curr_set:
                # We can add to set and recurse
                answer += 1
                curr_set.add(nums[curr_index])
                set_copy = curr_set.copy()
                answer += recursive(curr_index + 1, set_copy)
            return answer
        
        answer = 0
        for i in range(num_nums):
            current_set = set()
            current_set.add(nums[i])
            answer += 1
            answer += recursive(i + 1, current_set)
        return answer