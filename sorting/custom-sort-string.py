class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq_dict = {}
        for char in s:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
        
        answer = ""
        for char in order:
            if char in freq_dict:
                answer += (char * freq_dict[char])
        
        for char in freq_dict:
            if char not in order:
                answer += (char * freq_dict[char])
        return answer