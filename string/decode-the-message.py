class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        new_key = key.split(" ")
        new_key = ''.join(new_key)
        key_dict = {}
        # Start at 97
        curr_ascii = 97
        for char in new_key:
            if char not in key_dict:
                key_dict[char] = chr(curr_ascii)
                curr_ascii += 1

        answer = ""
        for char in message:
            if char == " ":
                answer += char
            else:
                answer += key_dict[char]
        return answer