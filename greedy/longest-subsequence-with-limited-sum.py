class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        nums.sort()
        for query in queries:
            i = 0
            curr_sum = 0
            while i < len(nums) and curr_sum + nums[i] <= query:
                curr_sum += nums[i]
                i += 1
            answer.append(i)
        return answer