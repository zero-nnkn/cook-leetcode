class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        final_intervals = []
        n = len(intervals)
        idx = 0

        # 1. Add all intervals before newInterval
        while idx < n and intervals[idx][1] < newInterval[0]:
            final_intervals.append(intervals[idx])
            idx += 1
        
        while idx < n and newInterval[1] >= intervals[idx][0]:
            newInterval = [
                min(newInterval[0], intervals[idx][0]),
                max(newInterval[1], intervals[idx][1])
            ]
            idx += 1
        final_intervals.append(newInterval)

        if idx < n:
            final_intervals.extend(intervals[idx:])

        return final_intervals




        

        