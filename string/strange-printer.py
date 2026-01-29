class Solution:
    def strangePrinter(self, s: str) -> int:
        memo_dict = {}
        # Going to try and solve printing for i to j
        def recursive(i, j):
            # If i > j, nothing to do
            if i > j:
                return 0
            elif (i, j) in memo_dict:
                return memo_dict[(i, j)]
            # Initially, our optimal solution is to print char once and add it to rest of string
            best = recursive(i + 1, j) + 1
            for k in range(i + 1, j + 1):
                # We could improve by writing multiple chars
                if s[k] == s[i]:
                    best = min(best, recursive(k + 1, j) + recursive(i, k - 1))
            memo_dict[(i, j)] = best
            return best
                    
            
        return recursive(0, len(s) - 1)