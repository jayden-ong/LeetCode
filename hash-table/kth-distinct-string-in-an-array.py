class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        word_dict = {}
        for word in arr:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        
        for word in arr:
            if word_dict[word] == 1:
                if k == 1:
                    return word
                else:
                    k -= 1
        return ""