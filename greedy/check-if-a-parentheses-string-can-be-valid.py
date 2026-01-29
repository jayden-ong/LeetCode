class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        changes_stack = []
        open_stack = []
        for i in range(len(s)):
            if locked[i] == '0':
                changes_stack.append(i)
            else:
                if s[i] == ")":
                    if len(open_stack) > 0:
                        open_stack.pop()
                    elif len(changes_stack) > 0:
                        changes_stack.pop()
                    else:
                        return False
                else:
                    open_stack.append(i)
        
        # Match each remaining open bracket with something that can changes
        changes_stack_index = len(changes_stack) - 1
        for i in range(len(open_stack) - 1, -1, -1):
            if changes_stack_index == -1 or changes_stack[changes_stack_index] < open_stack[i]:
                return False
            changes_stack_index -= 1

        return True


