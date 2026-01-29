class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        length_bits = len(bits)
        while i < length_bits:
            if i == length_bits - 1:
                return True
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return False