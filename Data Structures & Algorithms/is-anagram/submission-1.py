class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ref = []
        if len(s) == len(t) :
            for char in s  :
                ref.append(char)
            for char in t  : 
                if char  in ref  : 
                    ref.remove(char)
                else : 
                    return False
            return True 
        else : 
            return False