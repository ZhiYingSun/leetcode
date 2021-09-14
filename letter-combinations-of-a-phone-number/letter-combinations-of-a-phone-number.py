class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if len(digits) == 0:
            return result
        
        mapping = {
            0: '',
            1: '',
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'  
        }
        
        letterCombinationRecursive(result, digits, "", 0, mapping)
        return result

def letterCombinationRecursive(result, digits, current, index, mapping):
    # base case
    if index == len(digits):
        result.append(current)
        return 
    
    letters = mapping[int(digits[index])]
    
    for i in range(len(letters)):
        letterCombinationRecursive(result, digits, current + letters[i], index + 1, mapping)
            