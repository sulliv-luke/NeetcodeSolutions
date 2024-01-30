class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            # If both strings are different sizes, return false
            return False
        for i in set(s):
            # If there is a character in s with a different frequency in t, then return false
            if s.count(i) != t.count(i):
                return False
        # Otherwise, both strings are the same length and they have the same character frequencies, so its True
        return True