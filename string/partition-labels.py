class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters_dict = {}
        for i in range(len(s)):
            letters_dict[s[i]] = i

        starting_index = 0
        latest_index = None
        answer = []
        for i in range(len(s)):
            if latest_index is None:
                latest_index = letters_dict[s[i]]
            else:
                latest_index = max(latest_index, letters_dict[s[i]])
            
            if i >= latest_index:
                answer.append(latest_index - starting_index + 1)
                starting_index = i + 1
                latest_index = None
        return answer