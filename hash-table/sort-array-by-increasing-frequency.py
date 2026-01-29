from operator import itemgetter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        # First item is the number and the second is how many times it appears
        freq_list = []
        for key in freq_dict:
            freq_list.append((key, freq_dict[key]))
        
        freq_list = sorted(freq_list, key = itemgetter(0), reverse=True)
        freq_list = sorted(freq_list, key = itemgetter(1))
        answer = []
        for item in freq_list:
            answer += ([item[0]] * item[1])
        return answer