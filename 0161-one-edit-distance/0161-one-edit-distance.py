class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False

        len_s, len_t = len(s), len(t)

        if len_s - len_t == 1:
            # means that we can remove one char from s to make it equal t
            for i in range(len(s)):
                new_s = s[:i] + s[i+1:]
                if new_s == t:
                    return True
        elif len_t - len_s == 1:
            # means that we can insert one char to s to make it equal t
            for i in range(len(t)):
                new_t = t[:i] + t[i+1:]
                if new_t == s:
                    return True
        elif len_t == len_s:
            if len(s) == 1:
                return True
            pointer_s, pointer_t = 0,0
            diff =0

            while pointer_s < len(s):
                if s[pointer_s] != t[pointer_t]:
                    diff+=1
                pointer_s+=1
                pointer_t+=1
            if diff <=1:
                return True
        return False
