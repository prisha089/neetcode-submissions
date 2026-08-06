class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = sorted(s)
        list2= sorted(t)
        return list1==list2
    
        