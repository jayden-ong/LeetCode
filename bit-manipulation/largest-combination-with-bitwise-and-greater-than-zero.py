class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        '''
        answer_dict = {}
        def add_candidate(curr_index, curr_res, num_candidates):
            # Bitwise AND of 0 and any number is 0
            if curr_index == len(candidates) or curr_res == 0:
                return num_candidates
            
            if (curr_index, curr_res) in answer_dict:
                return answer_dict[(curr_index, curr_res)]
            
            # Try adding each one
            answer = num_candidates
            for i in range(curr_index, len(candidates)):
                if curr_res & candidates[i] != 0:
                    answer = max(answer, add_candidate(i + 1, curr_res & candidates[i], num_candidates + 1))
            answer_dict[(curr_index, curr_res)] = answer
            return answer
        
        answer = 0
        for i in range(len(candidates)):
            answer = max(answer, add_candidate(i + 1, candidates[i], 1))
        return answer
        '''

        answer_dict = defaultdict(int)
        answer = 0
        for candidate in candidates:
            binary_candidate = format(candidate, 'b')
            curr_bit = 0
            for i in range(len(binary_candidate) - 1, -1, -1):
                if binary_candidate[i] == "1":
                    answer_dict[curr_bit] += 1
                    answer = max(answer, answer_dict[curr_bit])
                curr_bit += 1
        return answer