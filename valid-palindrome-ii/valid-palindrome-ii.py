class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) -1
        
        while left < right:
            if s[left] != s[right]:
                s_1, s_2 = s[left:right], s[left + 1:right +1]
                return s_1 == s_1[::-1] or s_2 == s_2[::-1]
            left += 1
            right -=1
        return True
            