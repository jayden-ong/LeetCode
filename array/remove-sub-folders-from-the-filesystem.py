class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder, key=len)
        all_folders = set()
        answer = []
        for sub in folder:
            if len(all_folders) == 0:
                answer.append(sub)
            else:
                curr = "/"
                unique = True
                for i in range(1, len(sub)):
                    char = sub[i]
                    if char == "/" and curr in all_folders:
                        unique = False
                        break
                    curr += char
                
                if unique:
                    answer.append(sub)

            all_folders.add(sub)
        return answer