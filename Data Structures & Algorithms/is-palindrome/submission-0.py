class Solution:
    def isPalindrome(self, s: str) -> bool: 
        new_s = ""

        for char in s: 
            if char.isalnum(): 
                char = char.lower()
                new_s = new_s + char
        return new_s[::-1] == new_s

     
        