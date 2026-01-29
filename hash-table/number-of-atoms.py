class Solution:
    def countOfAtoms(self, formula: str) -> str:
        atoms_dict = {}
        def add_to_dict(atoms_dict, atom, num):
            if atom in atoms_dict:
                atoms_dict[atom] += num
            else:
                atoms_dict[atom] = num
        
        def handle_alpha(atoms_dict, curr_atom, i):
            # Current atom is not finished if the letter is lowercase
            if curr_atom != "" and not formula[i].islower():
                add_to_dict(atoms_dict, curr_atom, 1)

            if formula[i].isupper():
                return formula[i]
            
            return curr_atom + formula[i]

        def handle_formula(i):
            curr_atom = ""
            while i < len(formula):
                # If uppercase, consider it as new atom
                # If lowercase, part of last atom
                # Only reset curr_atom when we see a number
                if formula[i].isalpha():
                    curr_atom = handle_alpha(atoms_dict, curr_atom, i)
                elif formula[i].isnumeric():
                    curr_num = ""
                    while i < len(formula) and formula[i].isnumeric():
                        curr_num += formula[i]
                        i += 1
                    add_to_dict(atoms_dict, curr_atom, int(curr_num))
                    curr_atom = ""
                    i -= 1
                else:
                    if curr_atom != "":
                        add_to_dict(atoms_dict, curr_atom, 1)
                        curr_atom = ""
                    i, multiplied_atoms_dict = handle_bracket(i + 1)
                    for multiplied_atom in multiplied_atoms_dict:
                        add_to_dict(atoms_dict, multiplied_atom, multiplied_atoms_dict[multiplied_atom])
                i += 1
            
            # Last atom
            if curr_atom != "":
                add_to_dict(atoms_dict, curr_atom, 1)

        def handle_bracket(i):
            # Want to keep track of all atoms
            inner_dict = {}
            curr_atom = ""
            while True:
                # If uppercase, consider it as new atom
                # If lowercase, part of last atom
                # Only reset curr_atom when we see a number
                if formula[i].isalpha():
                    curr_atom = handle_alpha(inner_dict, curr_atom, i)
                elif formula[i].isnumeric():
                    curr_num = ""
                    while formula[i].isnumeric():
                        curr_num += formula[i]
                        i += 1
                    add_to_dict(inner_dict, curr_atom, int(curr_num))
                    curr_atom = ""
                    i -= 1
                else:
                    if curr_atom != "":
                        add_to_dict(inner_dict, curr_atom, 1)
                        curr_atom = ""
                    
                    if formula[i] == "(":
                        i, new_dict = handle_bracket(i + 1)
                        for new_atom in new_dict:
                            add_to_dict(inner_dict, new_atom, new_dict[new_atom])
                    else:
                        # Will add everything from inner_dict to atoms_dict
                        modifier = 1
                        dict_to_return = {}
                        if i + 1 < len(formula) and formula[i + 1].isnumeric():
                            curr_num = ""
                            i += 1
                            while i < len(formula) and formula[i].isnumeric():
                                curr_num += formula[i]
                                i += 1
                            modifier = int(curr_num)
                            i -= 2
                            
                        for inner_atom in inner_dict:
                            add_to_dict(dict_to_return, inner_atom, modifier * inner_dict[inner_atom])
                            
                        if modifier == 1:
                            return i, dict_to_return
                        else:
                            return i + 1, dict_to_return
                    
                i += 1
                print(inner_dict)
                print(i)
        
        handle_formula(0)
        # Error check
        # print(atoms_dict)
        atoms_heap = []
        for atom in atoms_dict:
            heapq.heappush(atoms_heap, (atom, atoms_dict[atom]))
        
        answer = ""
        while atoms_heap:
            curr_atom, curr_amount = heapq.heappop(atoms_heap)
            if curr_amount == 1:
                answer += curr_atom
            else:
                answer += curr_atom + str(curr_amount)

        return answer