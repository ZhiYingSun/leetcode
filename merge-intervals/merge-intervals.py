class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []                                                 # putting new interval into new list
        intervals.sort(key=lambda interval: interval[0])            # sort key parameter with lambda function
        
        for interval in intervals:
            if len(merged) == 0 or merged[-1][1] < interval[0]:     # merge is empty or current interval does
                merged.append(interval)                             # not overlap with the previous
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged