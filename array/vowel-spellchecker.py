class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        answer = []
        word_set = set()
        word_set_i = defaultdict(list)
        word_set_v = defaultdict(list)
        def convert_vowels(word):
            answer = ""
            for letter in word:
                if letter in "aeiouAEIOU":
                    answer += "*"
                else:
                    answer += letter.lower()
            return answer
        for word in wordlist:
            word_set.add(word)
            word_set_i[word.lower()].append(word)
            word_set_v[convert_vowels(word)].append(word)
        print(word_set_v)
        for query in queries:
            if query in word_set:
                answer.append(query)
                continue
            
            if query.lower() in word_set_i:
                answer.append(word_set_i[query.lower()][0])
                continue
            
            temp = convert_vowels(query)
            if temp in word_set_v:
                answer.append(word_set_v[temp][0])
                continue
            answer.append("")

        return answer