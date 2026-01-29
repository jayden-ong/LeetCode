class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        # There are at most 26 unique letters, so they can al fit in the same partition
        if k == 26:
            return 1
        
        left_mask = [0] * len(s)
        left_dupes = [0] * len(s)
        left_partitions = [0] * len(s)

        mask, dupes, partitions = 0, 0, 1
        for i, letter in enumerate(s):
            bit = 1 << (ord(letter) - ord('a'))
            dupes |= mask & bit
            mask |= bit
            # Reset -- we have to create a new partition
            if mask.bit_count() > k:
                mask, dupes, partitions = bit, 0, partitions + 1
            
            left_mask[i], left_dupes[i], left_partitions[i] = mask, dupes, partitions
        
        answer = partitions
        mask, dupes, partitions = 0, 0, 0
        for i in range(len(s) - 1, -1, -1):
            bit = 1 << ord(s[i]) - ord('a')
            dupes |= mask & bit
            mask |= bit

            bit_count = mask.bit_count()
            if bit_count > k:
                mask, dupes, partitions = bit, 0, partitions + 1
            
            if bit_count == k:
                if bit & dupes != 0 and bit & left_dupes[i] != 0 and left_mask[i].bit_count() == k and left_mask[i] | mask != 0x3FFFFFF:
                    answer = max(answer, partitions + left_partitions[i] + 2)
                elif dupes != 0:
                    answer = max(answer, partitions + left_partitions[i] + 1)
        return answer