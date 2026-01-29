class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dict = {'a' : ".-", 'b' : "-...", 'c' : "-.-.", 'd' : "-..",
                      'e' : ".", 'f' : "..-.", 'g' : "--.", 'h' : "....",
                      'i' : "..", 'j' : ".---", 'k' : "-.-", 'l' : ".-..",
                      'm' : "--", 'n' : "-.", 'o' : "---", 'p' : ".--.",
                      'q' : "--.-", 'r' : ".-.", 's' : "...", 't' : "-",
                      'u' : "..-", 'v' : "...-", 'w' : ".--", 'x' : "-..-", 'y' : "-.--", 'z': "--.."}
        transformations = {}
        num_unique = 0
        for word in words:
            curr_morse = ""
            for char in word:
                curr_morse += morse_dict[char]
            
            if curr_morse not in transformations:
                transformations[curr_morse] = True
                num_unique += 1
                
        return num_unique