class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Want to first get all the costs
        length_s = len(s)
        costs_list = []
        for i in range(length_s):
            costs_list.append(abs(ord(s[i]) - ord(t[i])))
        answer = 0
        curr_cost = 0
        window_size = 0
        curr_answer = 0
        # Go over all costs and see how far we make it
        for i in range(length_s):
            curr_index = i + window_size
            while curr_index < length_s:
                curr_cost += costs_list[curr_index]
                if curr_cost > maxCost:
                    break
                window_size += 1
                curr_index += 1
                curr_answer += 1
            answer = max(answer, curr_answer)
            # Reset for next iteration
            curr_cost -= costs_list[i]
        return answer