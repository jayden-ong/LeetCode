class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num_to_index = defaultdict(list)
        answer = [0] * len(nums)
        for i, num in enumerate(nums):
            for prev_index in num_to_index[num]:
                answer[prev_index] += abs(prev_index - i)
                answer[i] += abs(prev_index - i)
            num_to_index[num].append(i)
        return answer