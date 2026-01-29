class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        answer = 0
        def validate_dict(letters_dict):
            return letters_dict['a'] > 0 and letters_dict['b'] > 0 and letters_dict['c'] > 0
        
        vowels_dict = defaultdict(int)
        curr_end = 0
        for i in range(len(s)):
            while curr_end < len(s) and not validate_dict(vowels_dict):
                vowels_dict[s[curr_end]] += 1
                curr_end += 1
            
            if validate_dict(vowels_dict):
                answer += len(s) - curr_end + 1
            vowels_dict[s[i]] -= 1
        return answer
