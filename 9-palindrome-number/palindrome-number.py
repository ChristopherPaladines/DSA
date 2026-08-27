class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_integer = str(x)
        if string_integer == string_integer[::-1]:
            return True
        else:
            return False