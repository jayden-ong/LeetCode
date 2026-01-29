class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        def find_word(curr_string, desired_word):
            for i in range(len(curr_string)):
                if curr_string[i:i + len(desired_word)] == desired_word:
                    return i
            return -1
        
        answers_dict = {}
        def find_best_option(curr_string):
            if curr_string in answers_dict:
                return answers_dict[curr_string]
            
            best_option = len(curr_string)
            for word in dictionary:
                word_location = find_word(curr_string, word)
                if word_location != -1:
                    best_option = min(best_option, find_best_option(curr_string[:word_location]) + find_best_option(curr_string[word_location + len(word):]))
                    
            answers_dict[curr_string] = best_option
            return best_option
        
        return find_best_option(s)