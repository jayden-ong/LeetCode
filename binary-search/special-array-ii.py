class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        groups_dict = {}
        curr_group = 0
        groups_dict[0] = 0
        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                curr_group += 1
            groups_dict[i] = curr_group
        
        answer = []
        for start, end in queries:
            if groups_dict[start] == groups_dict[end]:
                answer.append(True)
            else:
                answer.append(False)
        return answer