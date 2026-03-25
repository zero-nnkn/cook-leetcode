class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]

        final_intervals = []
        idx = 0
        while idx < len(intervals) and newInterval[0] > intervals[idx][1]:
            final_intervals.append(intervals[idx])
            idx += 1

        if idx >= len(intervals):
            return intervals + [newInterval]
        
        while idx < len(intervals) and newInterval[1] >= intervals[idx][0]:
            newInterval = [
                min(newInterval[0], intervals[idx][0]),
                max(newInterval[1], intervals[idx][1])
            ]
            idx += 1

        final_intervals.append(newInterval)
        if idx < len(intervals):
            final_intervals.extend(intervals[idx:])

        return final_intervals




        

        