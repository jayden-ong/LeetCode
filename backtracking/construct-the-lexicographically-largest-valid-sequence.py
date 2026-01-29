class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        answer = [0] * (2 * (n - 1) + 1)
        numbers_used = set()
        def find_sequence(curr_index, answer, numbers_used):
            if curr_index == len(answer):
                return True
            
            # No need to continue if we have already filled the current pos
            if answer[curr_index] != 0:
                return find_sequence(curr_index + 1, answer, numbers_used)
            
            # Loop over all numbers starting from n and going down to 1
            for i in range(n, 0, -1):
                if i not in numbers_used:
                    numbers_used.add(i)
                    answer[curr_index] = i
                    # Special case since it only appears once
                    if i == 1:
                        if find_sequence(curr_index + 1, answer, numbers_used):
                            return True
                    elif curr_index + i < len(answer) and answer[curr_index + i] == 0:
                        answer[curr_index + i] = i
                        if find_sequence(curr_index + 1, answer, numbers_used):
                            return True
                        answer[curr_index + i] = 0
                    # If this is not ideal, undo
                    answer[curr_index] = 0
                    numbers_used.remove(i)
            return False
        find_sequence(0, answer, numbers_used)
        return answer
