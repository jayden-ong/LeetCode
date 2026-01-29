class Solution:
    def countSeniors(self, details: List[str]) -> int:
        answer = 0
        for detail in details:
            if int(detail[-4:-2]) > 60:
                answer += 1
        return answer