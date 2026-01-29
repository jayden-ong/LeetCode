class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # Want to find where the soonest 1 bits are for all positions
        one_bits_dict = {}
        answer = []
        for i in range(len(nums) - 1, -1, -1):
            binary_num = bin(nums[i])
            rev_binary_num = str(binary_num[2:])[::-1]
            
            for j in range(len(rev_binary_num)):
                if rev_binary_num[j] == "1":
                    one_bits_dict[j] = i
            
            worst_pos = i
            for bit in one_bits_dict:
                worst_pos = max(worst_pos, one_bits_dict[bit])
            
            answer.append(worst_pos - i + 1)
        return answer[::-1]
         