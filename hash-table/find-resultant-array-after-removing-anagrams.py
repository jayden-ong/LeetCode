class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        num_words = len(words)
        prev_dict = {}
        prev_word = words[0]
        for char in words[0]:
            if char in prev_dict:
                prev_dict[char] += 1
            else:
                prev_dict[char] = 1

        answer = [words[0]]
        for i in range(1, num_words):
            # Need to create a dictionary for index i
            new_dict = {}
            do_add = False
            if len(prev_word) != len(words[i]):
                do_add = True
            
            for char in words[i]:
                if char in new_dict:
                    new_dict[char] += 1
                else:
                    new_dict[char] = 1
                
                if char not in prev_dict or prev_dict[char] <= 0:
                    do_add = True
                else:
                    prev_dict[char] -= 1
            
            if do_add:
                answer.append(words[i])
            prev_dict = new_dict
            prev_word = words[i]
        return answer
