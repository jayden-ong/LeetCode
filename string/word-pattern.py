class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns_list = s.split(" ")
        pattern_dict = {}
        reverse_pattern_dict = {}
        i = 0
        num_patterns = len(patterns_list)
        for char in pattern:
            if i >= num_patterns:
                return False

            if char in pattern_dict:
                if pattern_dict[char] != patterns_list[i]:
                    return False
            else:
                pattern_dict[char] = patterns_list[i]
            
            if patterns_list[i] in reverse_pattern_dict:
                if reverse_pattern_dict[patterns_list[i]] != char:
                    return False
            else:
                reverse_pattern_dict[patterns_list[i]] = char
            
            i += 1
            
        return len(patterns_list) == i