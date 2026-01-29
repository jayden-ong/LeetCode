class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        length_path_list = len(path_list)
        answer = []
        for i in range(length_path_list):
            if path_list[i] == "":
                continue
            else:
                if path_list[i] == "..":
                    if len(answer) > 0:
                        answer.pop()
                elif path_list[i] != ".":
                    answer.append(path_list[i])
        
        if len(answer) == 0:
            return "/"
        
        new_path = ""
        for seg in answer:
            new_path += "/"
            new_path += seg
        return new_path
