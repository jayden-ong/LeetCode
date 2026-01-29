class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # If nums_used[i - 1] is False, "i" has not been used
        nums_used = [False] * 9
        answer = []
        def find_smallest_string(curr_index, nums_used):
            if curr_index == len(pattern):
                return True
            
            # There is no previous
            prev = None
            if answer != []:
                prev = answer[-1]
            
            if curr_index == -1:
                start = 0
                end = 9
            elif pattern[curr_index] == 'I':
                start = 0
                if prev is not None:
                    start = int(prev)
                end = 9
            else:
                end = 9
                if prev is not None:
                    end = int(prev)
                start = 0

            for num in range(start, end):
                if not nums_used[num]:
                    nums_used[num] = True
                    answer.append(str(num + 1))
                    if find_smallest_string(curr_index + 1, nums_used):
                        return True
                    answer.pop()
                    nums_used[num] = False

            return False
        
        find_smallest_string(-1, nums_used)
        return ''.join(answer)
            