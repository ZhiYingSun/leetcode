class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # take any string in the list and use it as a base
        # for every string after it, we keep making this shorter
        # untill all string pass and we will either have an empty or a longest common
        
        shortest = min(strs, key=len)
        
        for i, char in enumerate(shortest):
            for string in strs:
                if string[i] != char:
                    return shortest[:i]
        return shortest
            