class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        prev = set()
        answer = set()
        for num in arr:
            curr = set()
            curr.add(num)
            for pre in prev:
                curr.add(num | pre)
            answer.update(curr)
            prev = curr
        return len(answer)