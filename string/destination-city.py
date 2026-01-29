class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destinations_dict = set()
        for path in paths:
            destinations_dict.add(path[0])
        
        for path in paths:
            if path[1] not in destinations_dict:
                return path[1]