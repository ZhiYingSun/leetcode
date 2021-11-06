class Solution:
    def validPalindrome(self, s: str) -> bool:
        # first idea: find the first index not a palindrome, stop, remove it and then do valid Palindrome on it
        start = 0
        end = len(s) -1
        i_s = i_e = -1
        
        while start < end:
            if s[start] != s[end]:
                i_s = start
                i_e = end
                break
            start += 1
            end -= 1
        if i_s != -1:
            s_1 = s[0:i_s]  + s[(i_s+1)::]
        if i_e != -1:
            s_2 = s[0:i_e] + s[i_e+1::]
        if i_e == -1 and i_s == -1:
            return True
        
        start = 0
        end = len(s_1) -1
        s1_valid = True
        while start < end:
            if s_1[start] != s_1[end]:
                s1_valid = False
                break
            start += 1
            end -= 1 
        
        start = 0
        end = len(s_2) -1
        s2_valid = True
        while start < end:
            if s_2[start] != s_2[end]:
                s2_valid = False
                break
            start += 1
            end -= 1 
        
        return s1_valid or s2_valid
        
            