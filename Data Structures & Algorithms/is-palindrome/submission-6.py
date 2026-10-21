class Solution:
    def isPalindrome(self, s: str) -> bool: 
        new_s=""

        for a in s: 
            if a.isalnum(): 
                a = a.lower()
                new_s= new_s + a
        return new_s == new_s[::-1]



     
        