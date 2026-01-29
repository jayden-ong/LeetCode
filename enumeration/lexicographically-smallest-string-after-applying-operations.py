class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        answer = s
        # If b is odd, we can change any set of odd-indexed digits
        # If b is even, we can only change the initial set of odd-indexed digits

        # Want to make the first odd index 0 -- only impossible if a = 0 or 5
            #   If a is 1, 3, 7, 9 --> the digit can be reduced to 0 no matter what it is
            #   If a is 2, 4, 6, 8 --> the digit can only be reduced to 0 if it is also even
            #       Otherwise, the min digit is 1
            #   If a is 0 or 5 --> there is only one other option 
        
        # Get all possible starting_strings
        indexes_started = [False] * len(s)
        curr_index = 0
        while not indexes_started[curr_index]:
            indexes_started[curr_index] = True
            for j in range(10):
                limit = 9
                if b % 2 == 0:
                    limit = 0
                for k in range(limit + 1):
                    new_string = ""
                    curr_string = s[curr_index:] + s[:curr_index]
                    for i in range(len(s)):
                        if i % 2 == 1:
                            new_string += str((int(curr_string[i]) + j * a) % 10)
                        else:
                            new_string += str((int(curr_string[i]) + k * a) % 10)
                    
                    answer = min(answer, new_string)
            curr_index = (curr_index + b) % len(s)
        return answer