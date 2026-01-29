class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        split_key = s.split("-")
        all_chars = ''.join(split_key)
        num_chars = len(all_chars)
        chars_first = num_chars % k
        if chars_first == 0:
            chars_first = k
        curr_key = all_chars[:chars_first].upper()

        for i in range(chars_first, num_chars - k + 1, k):
            curr_key += "-" + all_chars[i:i+k].upper()
        return curr_key