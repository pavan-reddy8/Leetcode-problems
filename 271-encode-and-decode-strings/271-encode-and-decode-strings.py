class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        en = ""
        for s in strs:
            en += str(len(s)) + '#' + s

        return en

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        j = 0
        while i < len(s):
            if s[j] != '#':
                j+=1
            else:
                l = int(s[i:j])
                res.append(s[j+1:j+l+1])
                i = j+l+1
                j=i

        return res
                        
                    
                        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))