class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : 
            return False
        
        ref = list(s) 

        for char in t  : 
            if char in ref : 
                ref.remove(char)
            else : 
                return False 
        return True 

      