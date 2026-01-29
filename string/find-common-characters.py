class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        num_words = len(words)
        curr_dict = {}
        for i in range(len(words[0])):
            if words[0][i] in curr_dict:
                curr_dict[words[0][i]] += 1
            else:
                curr_dict[words[0][i]] = 1
        
        for i in range(1, num_words):
            temp_dict = {}
            for j in range(len(words[i])):
                if words[i][j] in temp_dict:
                    temp_dict[words[i][j]] += 1
                else:
                    temp_dict[words[i][j]] = 1
            
            temp_curr_dict = curr_dict.copy()
            curr_dict = {}
            for letter in temp_curr_dict:
                if letter in temp_dict:
                    curr_dict[letter] = min(temp_curr_dict[letter], temp_dict[letter])
        answer = []
        for letter in curr_dict:
            answer += [letter] * curr_dict[letter]
        return answer