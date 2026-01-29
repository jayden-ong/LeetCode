class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []

        # If we get to curr_index with a sum we have already seen that is a fail, no point in exploring
        # failures = {}
        def recursive(curr_index, curr_sum, curr_list):
            if curr_sum == target:
                answer.append(curr_list.copy())
                return
            elif curr_sum > target:
                return
            
            prev = -1
            for i in range(curr_index, len(candidates)):
                if candidates[i] != prev:
                    curr_list.append(candidates[i])
                    recursive(i + 1, curr_sum + candidates[i], curr_list)
                    curr_list.pop()
                    prev = candidates[i]
            return
        recursive(0, 0, [])
        return answer

