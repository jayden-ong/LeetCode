class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common_set = set()
        set_a = set()
        set_b = set()
        answer = []
        for i in range(len(A)):
            set_a.add(A[i])
            set_b.add(B[i])
            if A[i] in set_b:
                common_set.add(A[i])
            
            if B[i] in set_a:
                common_set.add(B[i])

            answer.append(len(common_set))
        return answer