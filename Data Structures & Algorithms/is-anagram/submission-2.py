from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        U -
            inputs: two strings (s and t)
            output: bool (True if anagrams, else false)
            Constraints: assume both strings are lowercase
            Edge cases: two empty strings -> True

        Plan -
            convert both s and t to frequency maps
            return true if the frequency maps are the same
            else false

        I - 

        """
        if len(s) != len(t):
            return False
        
        s_map = Counter(list(s))
        t_map = Counter(list(t))

        for char, value in s_map.items():
            if char not in t_map:
                return False
            if value != t_map[char]:
                return False

        return True