class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
            
        check_pos = 0
        for c in t:
            if c == s[check_pos]:
                check_pos += 1
                if check_pos == len(s):
                    return True
        
        return False
        