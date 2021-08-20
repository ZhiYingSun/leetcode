class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partition_lengths = []
        last_indexes = {c: i for i, c in enumerate(s)}   # pre-processing to obtain a dictionary of last indexes  
        
        start = 0
        while start < len(s):
            end = last_indexes[s[start]]
            curr = start
            while curr != end:
                end = max(end, last_indexes[s[curr]])
                curr += 1
            
            partition_lengths.append(curr - start + 1)
            start = curr + 1
        
        return partition_lengths