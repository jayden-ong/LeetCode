class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        num_nums = len(nums)
        answer = []
        for i in range(1 << num_nums):
            curr = []
            for j in range(num_nums):
                if (1 << j) & i != 0:
                    curr.append(nums[j])
            
            curr.sort()
            if curr not in answer:
                answer.append(curr)
        return answer