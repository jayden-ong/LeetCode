class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # mods
        # [4, 4, 4, 2, 4, 0]
        mods_dict = {}
        mods_dict[0] = 1
        curr = 0
        answer = 0
        for i in range(len(nums)):
            curr = (curr + nums[i]) % k
            if curr in mods_dict:
                answer += mods_dict[curr]
                mods_dict[curr] += 1
            else:
                mods_dict[curr] = 1
        return answer