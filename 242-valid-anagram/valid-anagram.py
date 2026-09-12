class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        my_set = set(s)
        # created set
        # char represents each element in s

        for char in my_set:
            if s.count(char) != t.count(char):
                return False
        return True
        