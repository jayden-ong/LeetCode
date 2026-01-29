class Solution:
    def sortString(self, s: str) -> str:
        letters_dict = {}
        length_s = 0
        for char in s:
            length_s += 1
            if char in letters_dict:
                letters_dict[char] += 1
            else:
                letters_dict[char] = 1
        
        letters_list = []
        num_unique = 0
        for letter in letters_dict:
            letters_list.append(letter)
            num_unique += 1
        letters_list.sort()

        i = 0
        increase = True
        elements_added = 0
        answer = ""
        while elements_added < length_s:
            if letters_dict[letters_list[i]] > 0:
                answer += letters_list[i]
                letters_dict[letters_list[i]] -= 1
                elements_added += 1
            
            if increase:
                if i == num_unique - 1:
                    increase = False
                else:
                    i += 1
            else:
                if i == 0:
                    increase = True
                else:
                    i -= 1
            
        return answer