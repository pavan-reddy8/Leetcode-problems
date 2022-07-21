class TrieNode:
    def __init__(self):
        self.children = {}
        self.last = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.last = True
        
    def search(self, word: str) -> bool:
        def dfs(root,j):
            cur = root
            n = len(word)
            for i in range(j,n):
                if word[i] == '.':
                    for child in cur.children.values():
                        if dfs(child,i+1):
                            return True
                    return False
                else:
                    if word[i] in cur.children:
                        cur = cur.children[word[i]]
                    else:
                        return False
            return cur.last

        return dfs(self.root,0)