class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split(" ")
        num_words = len(words)
        i = 0
        prev_num = None
        while i < num_words:
            if words[i].isnumeric():
                if prev_num is None:
                    prev_num = int(words[i])
                else:
                    if prev_num >= int(words[i]):
                        return False
                    prev_num = int(words[i])
            i += 1
        return True