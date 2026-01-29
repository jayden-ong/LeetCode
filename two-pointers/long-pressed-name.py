class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        length_name = len(name)
        length_typed = len(typed)
        name_pointer = 0
        typed_pointer = 0
        while name_pointer < length_name and typed_pointer < length_typed:
            if name[name_pointer] == typed[typed_pointer]:
                # need to count how many times that letter appears in both
                begin_letter = 0
                curr_letter = name[name_pointer]
                while name_pointer < length_name and name[name_pointer] == curr_letter:
                    begin_letter += 1
                    name_pointer += 1
                
                begin_typed = 0
                curr_letter = typed[typed_pointer]
                while typed_pointer < length_typed and typed[typed_pointer] == curr_letter:
                    begin_typed += 1
                    typed_pointer += 1
                
                if begin_typed < begin_letter:
                    return False
            else:
                return False
        if typed_pointer != length_typed or name_pointer != length_name:
            return False
        return True