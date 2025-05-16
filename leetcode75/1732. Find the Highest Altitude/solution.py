class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_altitude = 0
        max_altitude = 0
        for i in range(len(gain)):
            cur_altitude += gain[i]
            if cur_altitude > max_altitude:
                max_altitude = cur_altitude
        return max_altitude
        