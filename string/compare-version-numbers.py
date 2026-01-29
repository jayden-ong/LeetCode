class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        version1_length = len(version1_list)
        version2_length = len(version2_list)
        version1_index = 0
        version2_index = 0
        while version1_index < version1_length or version2_index < version2_length:
            if version2_index == version2_length:
                if int(version1_list[version1_index]) != 0:
                    return 1
                version1_index += 1
            elif version1_index == version1_length:
                if int(version2_list[version2_index]) != 0:
                    return -1
                version2_index += 1
            else:
                if int(version1_list[version1_index]) < int(version2_list[version2_index]):
                    return -1
                elif  int(version1_list[version1_index]) > int(version2_list[version2_index]):
                    return 1
                version1_index += 1
                version2_index += 1

        return 0