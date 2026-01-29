class Solution:
    def compress(self, chars: List[str]) -> int:
        index_to_replace = 0
        curr_char_index = 1
        streak = 1
        curr_char = chars[0]
        while curr_char_index < len(chars):
            if chars[curr_char_index] == curr_char:
                streak += 1
            else:
                chars[index_to_replace] = curr_char
                index_to_replace += 1
                if streak > 1:
                    if streak >= 10:
                        for digit in str(streak):
                            chars[index_to_replace] = str(digit)
                            index_to_replace += 1
                    else:
                        chars[index_to_replace] = str(streak)
                        index_to_replace += 1
                streak = 1
                curr_char = chars[curr_char_index]
            curr_char_index += 1
        
        chars[index_to_replace] = curr_char
        index_to_replace += 1
        if streak > 1:
            if streak >= 10:
                for digit in str(streak):
                    chars[index_to_replace] = str(digit)
                    index_to_replace += 1
            else:
                chars[index_to_replace] = str(streak)
                index_to_replace += 1
            
        return index_to_replace 