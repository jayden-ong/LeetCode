class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino_dict = {}
        answer = 0
        for domino in dominoes:
            if (domino[0], domino[1]) not in domino_dict and (domino[1], domino[0]) not in domino_dict:
                tup = (domino[0], domino[1])
                domino_dict[tup] = 1
            elif (domino[1], domino[0]) in domino_dict:
                tup = (domino[1], domino[0])
                answer += domino_dict[tup]
                domino_dict[tup] += 1
            elif (domino[0], domino[1]) in domino_dict:
                tup = (domino[0], domino[1])
                answer += domino_dict[tup]
                domino_dict[tup] += 1
        print(domino_dict)
        return answer