class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_index_map = {}
        
        for i in range(len(s)):
            if (s[i] not in char_index_map):
                char_index_map[s[i]] = i
            else:
                # we have seen this before, invalidate it
                char_index_map[s[i]] = -1
        
        first = float('inf')
        
        for char in char_index_map:
            if char_index_map[char] != -1:
                first = min(first, char_index_map[char])
                
        
        return first if first != float('inf') else -1
