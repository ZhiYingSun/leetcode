class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []         
            anagrams[sorted_word].append(word)
        
        for anagram in anagrams.values():
            result.append(anagram)
            
        return result