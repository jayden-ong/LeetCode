class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        target_dict = {}
        for char in target:
            if char in target_dict:
                target_dict[char] += 1
            else:
                target_dict[char] = 1
        
        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        answer = float('inf')
        for char in target_dict:
            if char not in s_dict:
                return 0
            else:
                answer = min(answer, s_dict[char] // target_dict[char])
        return answer