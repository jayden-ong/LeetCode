class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        '''
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
        '''
        sparse_max = [[0] * len(nums).bit_length() for _ in range(len(nums))]
        sparse_min = [[0] * len(nums).bit_length() for _ in range(len(nums))]
        for i, num in enumerate(nums):
            sparse_max[i][0] = sparse_min[i][0] = nums[i]
        
        for j in range(1, len(nums).bit_length()):
            next_index = 1 << (j - 1)
            for i in range(len(nums) - (1 << j) + 1):
                sparse_max[i][j] = max(sparse_max[i][j - 1], sparse_max[i + next_index][j - 1])
                sparse_min[i][j] = min(sparse_min[i][j - 1], sparse_min[i + next_index][j - 1])
        
        def get_max_min(left, right, is_max):
            index = (right - left + 1).bit_length() - 1
            if is_max:
                return max(sparse_max[left][index], sparse_max[right - (1 << index) + 1][index])
            return min(sparse_min[left][index], sparse_min[right - (1 << index) + 1][index])
        
        diffs_heap = [(-(get_max_min(left, len(nums) - 1, True) - get_max_min(left, len(nums) - 1, False)), left, len(nums) - 1) for left in range(len(nums))]
        heapq.heapify(diffs_heap)
        answer = 0
        while k:
            curr_val, left, right = heapq.heappop(diffs_heap)
            curr_val *= -1
            answer += curr_val
            k -= 1
            if right > left:
                heapq.heappush(diffs_heap, (-(get_max_min(left, right - 1, True) - get_max_min(left, right - 1, False)), left, right - 1))

        return answer