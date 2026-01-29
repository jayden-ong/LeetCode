class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        letters_dict = {}
        curr = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            elif s1[i] in letters_dict and s2[i] in letters_dict:
                if letters_dict[s1[i]] != letters_dict[s2[i]]:
                    temp = letters_dict[s2[i]]
                    for letter in letters_dict:
                        if letters_dict[letter] == temp:
                            letters_dict[letter] = letters_dict[s1[i]]
            elif s1[i] in letters_dict:
                letters_dict[s2[i]] = letters_dict[s1[i]]
            elif s2[i] in letters_dict:
                letters_dict[s1[i]] = letters_dict[s2[i]]
            else:
                letters_dict[s1[i]] = curr
                letters_dict[s2[i]] = curr
                curr += 1
            print(letters_dict)
        groupings = [[] for i in range(curr)]
        for letter in letters_dict:
            groupings[letters_dict[letter]].append(letter)
        
        grouping_mins = []
        for grouping in groupings:
            if grouping != []:
                grouping_mins.append(min(grouping))
            else:
                grouping_mins.append(-1)
        
        answer = ""
        for letter in baseStr:
            if letter in letters_dict:
                answer += grouping_mins[letters_dict[letter]]
            else:
                answer += letter
        return answer