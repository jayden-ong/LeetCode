class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        curr_res = 0
        for num in nums:
            curr_res ^= num
        
        answer = []
        for i in range(len(nums)):
            curr_res_binary = format(curr_res, 'b')
            temp = curr_res_binary[::-1]
            curr = ""
            for j in range(max(maximumBit, len(temp))):
                if j >= len(temp):
                    curr += "1"
                else:
                    if temp[j] == "0":
                        curr += "1"
                    else:
                        curr += "0"
            answer.append(int(curr[::-1], 2))
            curr_res ^= nums[len(nums) - i - 1]
        return answer