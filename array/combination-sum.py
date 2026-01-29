class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        num_candidates = len(candidates)

        def recursive(curr_index, curr_candidates, curr_sum):
            answer = []
            if curr_sum > target or curr_index >= num_candidates:
                return answer
            elif curr_sum == target:
                return [curr_candidates]
            
            # Can choose to add another instance of candidates[i]
            candidates_copy = curr_candidates.copy()
            candidates_copy.append(candidates[curr_index])
            answer += recursive(curr_index, candidates_copy, curr_sum + candidates[curr_index])

            # Can choose to move on to the next index
            candidates_copy = curr_candidates.copy()
            answer += recursive(curr_index + 1, candidates_copy, curr_sum)
            return answer

        for i in range(num_candidates):
            answer += recursive(i, [candidates[i]], candidates[i])
        return answer