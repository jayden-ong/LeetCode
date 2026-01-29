from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        letters = ['A', 'C', 'G', 'T']
        bank = set(bank)
        genes_explored = set()
        stack = deque()
        stack.append((0, startGene))
        genes_explored.add(startGene)

        if endGene not in bank:
            return -1
        
        while stack:
            curr_cost, curr_gene = stack.popleft()
            if curr_gene == endGene:
                return curr_cost
            
            for i in range(8):
                curr_letter = curr_gene[i]
                for letter in letters:
                    if i < 7:
                        new_gene = curr_gene[:i] + letter + curr_gene[i + 1:]
                    else:
                        new_gene = curr_gene[:i] + letter
                    
                    if letter != curr_letter and new_gene in bank and new_gene not in genes_explored:
                        stack.append((curr_cost + 1, new_gene))
                        genes_explored.add(new_gene)

        return -1