class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            # Increment for s, decrement for t
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        # If all counts are zero, it's a valid anagram
        for val in count:
            if val != 0:
                return False
                
        return True
        