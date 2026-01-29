class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # There's a decision to be made at the beginning that determines whether or not 
        # the problem is solvable

        # Try first index being 0/1
        for num in range(0, 2):
            first_val = num
            curr = num
            for i in range(len(derived) - 1):
                if (derived[i] == 0 and curr == 0) or (derived[i] == 1 and curr == 1):
                    curr = 0
                else:
                    curr = 1
        
            if curr ^ first_val == derived[-1]:
                return True
        
        return False