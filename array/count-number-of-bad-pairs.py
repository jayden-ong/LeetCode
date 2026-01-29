class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Need to store what the beginning would be if there were no bad pairs
        ideal_beginnings = defaultdict(int)
        ideal_beginnings[nums[0]] += 1
        answer = 0
        for i in range(1, len(nums)):
            potential_bad = i
            not_bad_pairs = ideal_beginnings[nums[i] - i]
            answer += potential_bad - not_bad_pairs
            ideal_beginnings[nums[i] - i] += 1
        return answer