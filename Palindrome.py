class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if s==s[::-1]:
            return True
        else:
            return False
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        rev = 0

        while x > 0:
            rev = rev * 10 + (x % 10)
            x = x/10

        if original == rev:
            return true
