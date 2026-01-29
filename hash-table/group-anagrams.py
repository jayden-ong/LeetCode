class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_dict = {}
        for word in strs:
            letters_list = [0] * 26
            for char in word:
                letter_index = ord(char) - 97
                letters_list[letter_index] += 1
                
            letters_tuple = tuple(letters_list)
            if letters_tuple in answer_dict:
                answer_dict[letters_tuple].append(word)
            else:
                answer_dict[letters_tuple] = [word]
        
        answer = []
        print(answer_dict)
        for key in answer_dict:
            answer.append(answer_dict[key])
        return answer