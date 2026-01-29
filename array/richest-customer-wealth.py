class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        answer = float('-inf')
        num_accounts = len(accounts)
        for i in range(num_accounts):
            answer = max(answer, sum(accounts[i]))
        return answer