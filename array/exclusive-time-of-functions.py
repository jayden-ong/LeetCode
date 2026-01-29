class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        answer = [0] * n
        # First log HAS to be a start
        call_stack = []
        for i in range(len(logs)):
            curr_id, status, curr_time = logs[i].split(":")
            curr_id = int(curr_id)
            curr_time = int(curr_time)
            if i == 0 or not call_stack:
                call_stack.append((curr_id, status, curr_time))
                prev_id, prev_status, prev_time = call_stack[-1]
            else:
                # No matter what, we are ending the exclusive time of previous call
                if status == "start":
                    # Be careful with starting, the ending
                    if prev_status == "end":
                        answer[prev_id] -= 1
                    answer[prev_id] += curr_time - prev_time

                    call_stack.append((curr_id, status, curr_time))
                    prev_id, prev_status, prev_time = call_stack[-1]
                else:
                    if prev_status == "start":
                        answer[curr_id] += 1
                    answer[curr_id] += curr_time - prev_time

                    call_stack.pop()
                    # Get the previous id from stack[-1]
                    # Get the previous time from this one
                    prev_time = curr_time
                    prev_status = status
                    # If this is false, will not go through here
                    if call_stack:
                        prev_id = call_stack[-1][0]
            #print(logs[i])
            #print(answer)
            #print('---')
                    
        return answer