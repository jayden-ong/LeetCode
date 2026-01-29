class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        letters_dict = defaultdict(int)
        num_success = 0
        for letter in s:
            letters_dict[letter] += 1
            if letters_dict[letter] == k:
                num_success += 1
        
        if num_success != 3:
            return -1
        
        # Want to remove unnecessary letters from letters_dict
        curr_index = 0
        answer = len(s)
        while curr_index < len(s):
            letters_dict[s[curr_index]] -= 1
            if letters_dict[s[curr_index]] < k:
                letters_dict[s[curr_index]] += 1
                break
            curr_index += 1
            answer = min(answer, len(s) - curr_index)

        for i in range(len(s)):
            letters_dict[s[i]] += 1

            while curr_index < len(s):
                letters_dict[s[curr_index]] -= 1
                if letters_dict[s[curr_index]] < k:
                    letters_dict[s[curr_index]] += 1
                    break
                curr_index += 1
                answer = min(answer, len(s) - curr_index + i + 1)
        return answer
        
