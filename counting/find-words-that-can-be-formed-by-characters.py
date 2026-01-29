class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_dict = {}
        for char in chars:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        
        answer = 0
        for word in words:
            char_dict_copy = char_dict.copy()
            curr_length = 0
            good_string = True
            for char in word:
                curr_length += 1
                if char not in char_dict_copy or char_dict_copy[char] <= 0:
                    good_string = False
                    break
                char_dict_copy[char] -= 1
            if good_string:
                answer += curr_length
        return answer
