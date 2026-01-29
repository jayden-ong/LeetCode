class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Use ord(char) - 97 to get index in score
        # Want to form a dict of letters
        letters_dict = {}
        for char in letters:
            if char in letters_dict:
                letters_dict[char] += 1
            else:
                letters_dict[char] = 1
        
        # If valid, return score, curr_dict else return -1
        def is_valid(word, word_dict):
            curr_score = 0
            for char in word:
                if char not in word_dict or word_dict[char] <= 0:
                    return -1
                else:
                    curr_score += score[ord(char) - 97]
                    word_dict[char] -= 1
            return curr_score

        # Have to have current word index, current list of letters, and curr score
        def recursive(curr_index, curr_dict, curr_score):
            # No score if current index surpasses list
            if curr_index >= len(words):
                return curr_score
            
            # For each word, could add, could skip
            curr_dict_copy = curr_dict.copy()
            first_case = recursive(curr_index + 1, curr_dict_copy, curr_score)

            # Could add
            # curr_dict_copy = curr_dict.copy()
            word_score = is_valid(words[curr_index], curr_dict)
            second_case = 0
            if word_score > -1:
                # print(words[curr_index])
                second_case = recursive(curr_index + 1, curr_dict, curr_score + word_score)
            return max(first_case, second_case)
        
        answer = 0
        # print(letters_dict)
        for i in range(len(words)):
            letters_dict_copy = letters_dict.copy()
            curr_score = is_valid(words[i], letters_dict_copy)
            # Is valid, start with recursion
            if curr_score != -1:
                # print(words[i])
                print('---')
                highest_score = recursive(i + 1, letters_dict_copy, curr_score)
                answer = max(answer, highest_score)
        
        return answer