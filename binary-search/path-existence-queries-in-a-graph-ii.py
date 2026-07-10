class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        val_to_new_index = {}
        index_to_old_val = {}
        for i, num in enumerate(nums):
            index_to_old_val[i] = num
        
        prefix_sum = []
        nums.sort()
        for i, num in enumerate(nums):
            val_to_new_index[nums[i]] = i
            if i == 0:
                prefix_sum.append(0)
            else:
                if nums[i] - nums[i - 1] <= maxDiff:
                    prefix_sum.append(prefix_sum[-1] + 1)
                else:
                    prefix_sum.append(prefix_sum[-1])
        
        answer = []
        for left, right in queries:
            actual_left_value = prefix_sum[val_to_new_index[index_to_old_val[left]]]
            actual_right_value = prefix_sum[val_to_new_index[index_to_old_val[right]]]
            if abs(actual_right_value - actual_left_value) == abs(val_to_new_index[index_to_old_val[right]] - val_to_new_index[index_to_old_val[left]]):
                if left == right:
                    answer.append(0)
                elif index_to_old_val[right] == index_to_old_val[left]:
                    answer.append(1)
                else:
                    answer.append(math.ceil(abs(index_to_old_val[right] - index_to_old_val[left]) / maxDiff))
            else:
                answer.append(-1)
        return answer