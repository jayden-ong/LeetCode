class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        answer = []
        length_s = len(s)
        for i in range(0, length_s, k):
            string_to_add = s[i:i + k]
            if i + k > length_s:
                #print(string_to_add)
                string_to_add += fill * (i + k - length_s)
            answer.append(string_to_add)
        return answer