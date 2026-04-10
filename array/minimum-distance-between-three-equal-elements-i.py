class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        nums_dict = defaultdict(list)
        for i, num in enumerate(nums):
            nums_dict[num].append(i)
        
        answer = float('inf')
        for num in nums_dict:
            if len(nums_dict[num]) >= 3:
                for i in range(len(nums_dict[num])):
                    for j in range(i + 1, len(nums_dict[num])):
                        for k in range(j + 1, len(nums_dict[num])):
                            answer = min(answer, abs(nums_dict[num][i] - nums_dict[num][j]) + abs(nums_dict[num][j] - nums_dict[num][k]) + abs(nums_dict[num][i] - nums_dict[num][k]))
        if answer == float('inf'):
            return -1
        return answer