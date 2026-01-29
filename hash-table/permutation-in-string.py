class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_dict = {}
        for char in s1:
            if char in s1_dict:
                s1_dict[char] += 1
            else:
                s1_dict[char] = 1
        
        for i in range(len(s1)):
            if s2[i] in s1_dict:
                s1_dict[s2[i]] -= 1
        
        def get_mistakes(curr_dict):
            answer = 0
            for key in curr_dict:
                answer += abs(curr_dict[key])
            return answer

        if get_mistakes(s1_dict) == 0:
            return True

        for i in range(len(s1), len(s2)):
            # Remove first letter in window
            if s2[i - len(s1)] in s1_dict:
                s1_dict[s2[i - len(s1)]] += 1
            
            # Add current letter
            if s2[i] in s1_dict:
                s1_dict[s2[i]] -= 1
            
            if get_mistakes(s1_dict) == 0:
                return True
        return False