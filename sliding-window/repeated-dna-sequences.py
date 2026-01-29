class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        dna_set = set()
        answer = set()
        curr_dna = s[:10]
        dna_set.add(curr_dna)
        for i in range(10, len(s)):
            curr_dna = curr_dna[1:] + s[i]
            if curr_dna in dna_set:
                answer.add(curr_dna)
            dna_set.add(curr_dna)
        return list(answer)