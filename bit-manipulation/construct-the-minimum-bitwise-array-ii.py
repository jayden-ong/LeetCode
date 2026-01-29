class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            # 2 is the only even prime and cannot be constructed
            if num % 2 == 0:
                answer.append(-1)
                continue
            
            # Once we find the 0 bit, unset the one to the right
            bin_num = str(bin(num)[2:])
            last_zero = -1
            for i, digit in enumerate(bin_num):
                if digit == '0':
                    last_zero = i
            
            if last_zero == -1:
                answer.append(int(bin_num[1:], 2))
            else:
                curr = bin_num[:last_zero + 1] + "0"
                if last_zero + 2 < len(bin_num):
                    curr += bin_num[last_zero + 2:]
                answer.append(int(curr, 2))


        return answer