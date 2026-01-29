class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Stores all the people that trust someone else
        # Must be exactly n - 1
        people_trust_dict = {}
        num_people_trust = 0
        
        # Someone must be trusted n - 1 times
        people_trusted = {}
        max_trusted = 0
        curr_cand = 1
        for relationship in trust:
            if relationship[0] not in people_trust_dict:
                people_trust_dict[relationship[0]] = True
                num_people_trust += 1
            
            if relationship[1] not in people_trusted:
                people_trusted[relationship[1]] = 1
            else:
                people_trusted[relationship[1]] += 1

            if people_trusted[relationship[1]] > max_trusted:
                max_trusted = people_trusted[relationship[1]]
                curr_cand = relationship[1]
        
        # If the most anyone was trusted is not n - 1, there is no one everyone but one trusts
        if max_trusted != n - 1:
            return -1
        # If the cand is in the dictionary, that violates condition 1
        if curr_cand not in people_trust_dict:
            return curr_cand
        return -1