from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        combos_used = {}
        for deadend in deadends:
            combos_used[deadend] = True
        lock_stack = deque()
        lock_stack.append(("0000", 0))
        while lock_stack:
            curr_combo, curr_rotations = lock_stack.popleft()
            # Consider doing your checks before you add anything
            if curr_combo == target:
                return curr_rotations
            
            if curr_combo not in combos_used:
                # Need to add all possible rotations
                # First slot - backward
                if int(curr_combo[0]) == 0:
                    lock_stack.append(('9' + curr_combo[1:], curr_rotations + 1))
                else:
                    lock_stack.append((str(int(curr_combo[0]) - 1) + curr_combo[1:], curr_rotations + 1))
                # forward
                if int(curr_combo[0]) == 9:
                    lock_stack.append(('0' + curr_combo[1:], curr_rotations + 1))
                else:
                    lock_stack.append((str(int(curr_combo[0]) + 1) + curr_combo[1:], curr_rotations + 1))
                
                # Second slot - backward
                if int(curr_combo[1]) == 0:
                    lock_stack.append((curr_combo[0] + '9' + curr_combo[2:], curr_rotations + 1))
                else:
                    lock_stack.append((curr_combo[0] + str(int(curr_combo[1]) - 1) + curr_combo[2:], curr_rotations + 1))
                # Forward
                if int(curr_combo[1]) == 9:
                    lock_stack.append((curr_combo[0] + '0' + curr_combo[2:], curr_rotations + 1))
                else:
                    lock_stack.append((curr_combo[0] + str(int(curr_combo[1]) + 1) + curr_combo[2:], curr_rotations + 1))
                
                # Third slot - backward
                if int(curr_combo[2]) == 0:
                    lock_stack.append((curr_combo[:2] + '9' + curr_combo[3], curr_rotations + 1))
                else:
                    lock_stack.append((curr_combo[:2] + str(int(curr_combo[2]) - 1) + curr_combo[3], curr_rotations + 1))
                # Forward
                if int(curr_combo[2]) == 9:
                    lock_stack.append((curr_combo[:2] + '0' + curr_combo[3], curr_rotations + 1))
                else:
                    lock_stack.append((curr_combo[:2] + str(int(curr_combo[2]) + 1) + curr_combo[3], curr_rotations + 1))
                
                # Third slot - backward
                if int(curr_combo[3]) == 0:
                    lock_stack.append((curr_combo[:3] + '9', curr_rotations + 1))
                else:
                    lock_stack.append((curr_combo[:3] + str(int(curr_combo[3]) - 1), curr_rotations + 1))
                # Forward
                if int(curr_combo[3]) == 9:
                    lock_stack.append((curr_combo[:3] + '0', curr_rotations + 1))
                else:
                    lock_stack.append((curr_combo[:3] + str(int(curr_combo[3]) + 1), curr_rotations + 1))
            combos_used[curr_combo] = True

        return -1
        