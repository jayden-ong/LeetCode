class Solution:
    def originalDigits(self, s: str) -> str:
        letters_dict = {}
        for letter in s:
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
        
        # zero, one, two, three, four, five, six, seven, eight, nine
        answer = ""
        answer_list = [0] * 10 
        # For each "z", there must be 1 e, 1 r, 1 o
        if "z" in letters_dict:
            answer_list[0] = letters_dict['z']
            letters_dict['e'] -= letters_dict['z']
            letters_dict['r'] -= letters_dict['z']
            letters_dict['o'] -= letters_dict['z']
            letters_dict['z'] -= letters_dict['z']
        
        if "w" in letters_dict:
            answer_list[2] = letters_dict['w']
            letters_dict['t'] -= letters_dict['w']
            letters_dict['o'] -= letters_dict['w']
            letters_dict['w'] -= letters_dict['w']
            
        if "u" in letters_dict:
            answer_list[4] = letters_dict['u']
            letters_dict['f'] -= letters_dict['u']
            letters_dict['r'] -= letters_dict['u']
            letters_dict['o'] -= letters_dict['u']
            letters_dict['u'] -= letters_dict['u']
        
        if 'x' in letters_dict:
            answer_list[6] = letters_dict['x']
            letters_dict['i'] -= letters_dict['x']
            letters_dict['s'] -= letters_dict['x']
            letters_dict['x'] -= letters_dict['x']
        
        if 'g' in letters_dict:
            answer_list[8] = letters_dict['g']
            letters_dict['e'] -= letters_dict['g']
            letters_dict['i'] -= letters_dict['g']
            letters_dict['h'] -= letters_dict['g']
            letters_dict['t'] -= letters_dict['g']
            letters_dict['g'] -= letters_dict['g']
        
        if 'r' in letters_dict and letters_dict['r'] > 0:
            answer_list[3] = letters_dict['r']
            letters_dict['t'] -= letters_dict['r']
            letters_dict['h'] -= letters_dict['r']
            letters_dict['e'] -= 2 * letters_dict['r']
            letters_dict['r'] -= letters_dict['r']
            
        if 'o' in letters_dict and letters_dict['o'] > 0:
            answer_list[1] = letters_dict['o']
            letters_dict['n'] -= letters_dict['o']
            letters_dict['e'] -= letters_dict['o']
            letters_dict['o'] -= letters_dict['o']
        
        if 'f' in letters_dict and letters_dict['f'] > 0:
            answer_list[5] = letters_dict['f']
            letters_dict['i'] -= letters_dict['f']
            letters_dict['v'] -= letters_dict['f']
            letters_dict['e'] -= letters_dict['f']
            letters_dict['f'] -= letters_dict['f']
        
        if 's' in letters_dict and letters_dict['s'] > 0:
            answer_list[7] = letters_dict['s']
            letters_dict['e'] -= 2 * letters_dict['s']
            letters_dict['v'] -= letters_dict['s']
            letters_dict['n'] -= letters_dict['s']
            letters_dict['s'] -= letters_dict['s']
        
        if 'i' in letters_dict and letters_dict['i'] > 0:
            answer_list[9] = letters_dict['i']
            letters_dict['n'] -= 2 * letters_dict['i']
            letters_dict['e'] -= letters_dict['i']
            letters_dict['i'] -= letters_dict['i']
        
        for i in range(len(answer_list)):
            answer += str(i) * answer_list[i]
        return answer
            