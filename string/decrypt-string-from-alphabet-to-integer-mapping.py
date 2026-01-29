class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet_dict = {'1' : 'a', '2' : 'b', '3' : 'c', '4' : 'd',
                         '5' : 'e', '6' : 'f', '7' : 'g', '8' : 'h', 
                         '9' : 'i', '10#' : 'j', '11#' : 'k', '12#' : 'l',
                         '13#' : 'm', '14#' : 'n', '15#' : 'o', '16#' : 'p', 
                         '17#' : 'q', '18#' : 'r', '19#' : 's', '20#' : 't',
                         '21#' : 'u', '22#' : 'v', '23#' : 'w', '24#' : 'x', 
                         '25#' : 'y', '26#' : 'z'}
        
        # All characters that end with hash begin with 1 or 2
        i = 0
        length_s = len(s)
        answer = ""
        while i < length_s:
            # Nothing after if i is the last index
            if (s[i] == '1' or s[i] == '2') and i != length_s - 1:
                if i + 2 < length_s and s[i + 2] == "#":
                    answer += alphabet_dict[s[i:i + 3]]
                    i += 3
                else:
                    answer += alphabet_dict[s[i]]
                    i += 1
            else:
                answer += alphabet_dict[s[i]]
                i += 1
        return answer