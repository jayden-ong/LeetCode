class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 01 XOR 11 = 10
        # 010 XOR 001 -> 011 XOR 011 -> 000 XOR 100 -> 100
        # 010
        # 001
        # 011
        # 100 = 
        # 100 when we want 001
        # 110 XOR 001 -> 111 XOR 010 -> 101 XOR 100 -> 001
        # 100 XOR 100 -> 0
        # A number XOR itself will result in 0, a number XOR 0 is itself
        # An odd amount of 1s in a bit slot results in that bit slot being 1
        # An even amount of 1s in a bit slot results in that bit slot being 0
        # To get XOR, do ^
        curr = 0
        for num in nums:
            curr = curr ^ num
        binary_k = format(k, "b")
        length_k = len(binary_k)
        i = length_k - 1
        binary_curr = format(curr, "b")
        length_curr = len(binary_curr)
        j = length_curr - 1
        num_swaps = 0
        while i > -1 or j > -1:
            if i == -1:
                if binary_curr[j] == "1":
                    num_swaps += 1
                j -= 1
            elif j == -1:
                if binary_k[i] == "1":
                    num_swaps += 1
                i -= 1
            else:
                if binary_curr[j] != binary_k[i]:
                    num_swaps += 1
                i -= 1
                j -= 1
        return num_swaps
