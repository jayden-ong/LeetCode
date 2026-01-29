class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefixes_dict = defaultdict(int)
        for word in words:
            curr = ""
            for char in word:
                curr += char
                prefixes_dict[curr] += 1
        
        answer = []
        for word in words:
            curr = ""
            curr_answer = 0
            for char in word:
                curr += char
                curr_answer += prefixes_dict[curr]
            answer.append(curr_answer)
        return answer