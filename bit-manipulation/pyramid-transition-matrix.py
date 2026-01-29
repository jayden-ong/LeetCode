class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_dict = defaultdict(set)
        for string in allowed:
            allowed_dict[string[:2]].add(string[-1])
        
        def make_choice(line_below, curr_index, length_required, curr_line):
            if length_required == 1:
                if len(allowed_dict[line_below]) > 0:
                    return True
                return False
            
            curr_blocks = line_below[curr_index:curr_index + 2]
            for match in allowed_dict[curr_blocks]:
                # Start a new line
                if len(curr_line) == length_required - 1:
                    result = make_choice(curr_line + match, 0, length_required - 1, "")
                else:
                    result = make_choice(line_below, curr_index + 1, length_required, curr_line + match)
                
                if result:
                    return True
            return False

        return make_choice(bottom, 0, len(bottom) - 1, "")