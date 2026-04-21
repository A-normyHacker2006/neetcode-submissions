class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if not s  or s.isalpha() : 
        #     return False
        # The key point to this palindrome in python isalnum() That chackes if a string is all alpha or all num 
        x = ''.join(char.lower() for char in s  if char.isalnum())
        return x == x[::-1]