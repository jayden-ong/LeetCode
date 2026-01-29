class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        min_appear = len(nums) // 3
        answer = []
        for key in freq_dict:
            if freq_dict[key] > min_appear:
                answer.append(key)
        return answer
            