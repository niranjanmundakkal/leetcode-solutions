class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))
        n = intervals[0]
        i = 1
        while i<len(intervals):
            if intervals[i][1]<=n[1]:
                intervals.pop(i)
            else:

                n=intervals[i]
                i+=1
        return  len(intervals)