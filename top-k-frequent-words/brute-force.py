class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # dictionary word and number of occurences
        # a list to store the dictionary of words in order
        # retrive tuple of (word, number of occurences) from dictionary and then sort it
        
        freq = {}
        freq_list = {}
        result = []
        top_k = []
        for word in words:
            if word not in freq:
                freq[word] = 0
            freq[word] += 1
        
        
        # dictionary key: num occurences value: [words]
        for key in freq:
            if freq[key] not in freq_list:
                freq_list[freq[key]] = []
            freq_list[freq[key]].append(key)
        
        top_k = sorted(freq_list.keys())
        top_k.reverse()
        top_k = top_k[0:k]
        
        for key in top_k:
            temp = sorted(freq_list[key])
            result.extend(temp)
    
        return result[0:k]
        
        
