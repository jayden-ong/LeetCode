class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                depth -= 1
                if depth < 0:
                    depth = 0
            elif log == "./":
                continue
            else:
                depth += 1
        return depth