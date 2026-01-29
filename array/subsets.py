class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        num_nums = len(nums)
        # Any iteration with one 1 bit will always include only one item in curr_list
        for i in range(1 << num_nums):
            curr_list = []
            for j in range(num_nums):
                if (i & (1 << j)):
                    curr_list.append(nums[j])
            answer.append(curr_list)
        return answer