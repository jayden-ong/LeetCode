class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # The goal is to find the optimal starting point
        max_energy = energy.copy()
        for i in range(len(max_energy) - 1, -1, -1):
            if i + k < len(max_energy):
                max_energy[i] += max_energy[i + k]
        return max(max_energy)