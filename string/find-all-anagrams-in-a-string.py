class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_dict = {}
        for letter in p:
            if letter in p_dict:
                p_dict[letter] += 1
            else:
                p_dict[letter] = 1
        
        num_wrong = 0
        answer = []
        for i in range(len(p)):
            if s[i] not in p_dict:
                num_wrong += 1
            else:
                if p_dict[s[i]] <= 0:
                    num_wrong += 2
                p_dict[s[i]] -= 1
        
        if num_wrong == 0:
            answer.append(0)
        
        for i in range(len(p), len(s)):
            # sliding window - get rid of i - len(p)
            if s[i - len(p)] in p_dict:
                num_wrong -= abs(p_dict[s[i - len(p)]])
                p_dict[s[i - len(p)]] += 1
                num_wrong += abs(p_dict[s[i - len(p)]])
            
            if s[i] in p_dict:
                num_wrong -= abs(p_dict[s[i]])
                p_dict[s[i]] -= 1
                num_wrong += abs(p_dict[s[i]])
            
            if num_wrong == 0:
                answer.append(i - len(p) + 1)
        return answer