class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        answer_dict = {}
        answer = 0
        letters_seen = set()
        letter_dict = {}
        for i in range(len(s)):
            # Automatically, the letter on its own is a substring
            if i == 0:
                answer_dict[i] = 1
            else:
                if (s[i - 1] == "z" and s[i] == "a") or (ord(s[i]) - ord(s[i - 1])) == 1:
                    answer_dict[i] = answer_dict[i - 1] + 1
                else:
                    answer_dict[i] = 1
            
            if s[i] in letter_dict:
                letter_dict[s[i]] = max(letter_dict[s[i]], answer_dict[i])
            else:
                letter_dict[s[i]] = answer_dict[i]
        
        answer = 0
        for letter in letter_dict:
            answer += letter_dict[letter]
            
        return answer