class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# STRINGS ARE IMMUTABLE, THEY RETURN SMTH NEW THAT WAS CREATED