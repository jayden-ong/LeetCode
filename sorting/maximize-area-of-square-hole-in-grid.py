class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        def get_longest_consecutive_sequence(bars):
            start = end = 0
            answer = [0, 0]
            for i in range(len(bars)):
                if i != len(bars) - 1 and bars[i + 1] - bars[i] == 1:
                    end = i + 1
                else:
                    if end - start >= answer[1] - answer[0]:
                        answer[0], answer[1] = start, end
                    start = i + 1
            return answer

        h1, h2 = get_longest_consecutive_sequence(hBars)
        v1, v2 = get_longest_consecutive_sequence(vBars)
        return min(h2 - h1 + 2, v2 - v1 + 2) ** 2