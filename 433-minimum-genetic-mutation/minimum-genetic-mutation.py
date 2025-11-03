from collections import deque

class Solution:
    def minMutation(self, startGene, endGene, bank):
        bank = set(bank)
        if endGene not in bank:
            return -1
        
        gene_chars = ['A', 'C', 'G', 'T']
        begin = {startGene}
        end = {endGene}
        visited = set()
        steps = 0
        
        while begin and end:
            # Always expand the smaller frontier
            if len(begin) > len(end):
                begin, end = end, begin
            
            temp = set()
            for gene in begin:
                for i, c in enumerate(gene):
                    for ch in gene_chars:
                        if ch == c:
                            continue
                        mutated = gene[:i] + ch + gene[i+1:]
                        if mutated in end:
                            return steps + 1
                        if mutated in bank and mutated not in visited:
                            visited.add(mutated)
                            temp.add(mutated)
            begin = temp
            steps += 1
        
        return -1
