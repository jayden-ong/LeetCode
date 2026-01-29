class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = pow(10, 9) + 7
        hFences.append(1)
        hFences.sort()
        hFences.append(m)
        vFences.append(1)
        vFences.sort()
        vFences.append(n)
        def find_all_lengths(fences):
            answer = set()
            for i in range(len(fences) - 1):
                for j in range(i + 1, len(fences)):
                    answer.add(fences[j] - fences[i])
            return answer
        hFences_lengths = find_all_lengths(hFences)
        vFences_lengths = find_all_lengths(vFences)
        answer = -1
        for length in hFences_lengths:
            if length in vFences_lengths:
                answer = max(answer, length ** 2)
        if answer == -1:
            return answer
        return answer % MOD