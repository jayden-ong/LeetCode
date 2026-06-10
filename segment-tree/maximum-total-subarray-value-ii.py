class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max_diffs_heap = []
        diff_combinations = defaultdict(int)
        for i in range(len(nums)):
            curr_min = curr_max = nums[i]
            for j in range(i, len(nums)):
                curr_min = min(curr_min, nums[j])
                curr_max = max(curr_max, nums[j])
                if -(curr_max - curr_min) not in diff_combinations:
                    heapq.heappush(max_diffs_heap, -(curr_max - curr_min))
                diff_combinations[-(curr_max - curr_min)] += 1

        num_selections = k
        answer = 0
        while num_selections > 0:
            curr_diff = heapq.heappop(max_diffs_heap)
            answer += min(num_selections, diff_combinations[curr_diff]) * -curr_diff
            num_selections -= min(num_selections, diff_combinations[curr_diff])
        return answer