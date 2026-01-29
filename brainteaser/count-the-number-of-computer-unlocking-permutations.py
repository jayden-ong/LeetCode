class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = pow(10, 9) + 7
        # Index 0 is always the first computer to be decrypted
        # Keep track of all computers that can be opened by other computers?
        # You can unlock all of the computers as long as index 0 is the smallest complexity
        # That means that you can unlock any computer in any order?
        nums_dict = defaultdict(int)
        for num in complexity:
            nums_dict[num] += 1
        
        if complexity[0] != min(complexity) or nums_dict[complexity[0]] >= 2:
            return 0
        
        return math.factorial(len(complexity) - 1) % MOD