class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        def choice(curr_index, curr_list):
            copy = tuple(curr_list.copy())
            if len(curr_list) >= 2 and copy not in answer:
                answer.add(copy)
            
            if curr_index >= len(nums):
                return
            
            if nums[curr_index] >= curr_list[-1]:
                choice(curr_index + 1, curr_list + [nums[curr_index]])
            choice(curr_index + 1, curr_list)
            return

        for i in range(len(nums)):
            choice(i + 1, [nums[i]])
        
        new_answer = []
        for tup in answer:
            new_answer.append(list(tup))
        return new_answer