class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # We want to know what characters are at each index and how many times it appears at the index
        characters_dict = defaultdict(int)
        for word in words:
            for i, char in enumerate(word):
                characters_dict[(char, i)] += 1
        
        # Can store a dict that contains what the index of target is and the index of the character in words
        # For example, (1, 3) means we have the answer for everything starting at the first character of target
        # starting at the third character of any of the words
        dp = {}
        def choice(curr_word_index, curr_target_index):
            # Means we are done and we have formed the target
            if curr_target_index == len(target):
                dp[(curr_target_index, curr_word_index)] = 1
                return 1
            
            # Means we have not formed the word and we can no longer do so
            if curr_word_index == len(words[0]) or len(words[0]) - curr_word_index < len(target) - curr_target_index:
                return 0
            
            if (curr_target_index, curr_word_index) in dp:
                return dp[(curr_target_index, curr_word_index)]
            
            answer = 0
            desired_char = target[curr_target_index]
            # Our options are to go over all remaining word indices and if the character we want exists, we explore
            # If there is no way to form the current letter at the current word index, looking into dp, just break
            for i in range(curr_word_index, len(words[0])):
                if characters_dict[(desired_char, i)] > 0:
                    pre_answer = answer
                    if (curr_target_index, i) in dp:
                        answer += (characters_dict[(desired_char, i)] * dp[(curr_target_index, i)])
                    else:
                        answer += (characters_dict[(desired_char, i)] * choice(i + 1, curr_target_index + 1))
                    
                    # If our answer doesn't change, no point in exploring the rest of the options
                    if pre_answer == answer:
                        break
            
            dp[(curr_target_index, curr_word_index)] = answer
            return answer

        answer = choice(0, 0)
        return answer % (pow(10, 9) + 7)