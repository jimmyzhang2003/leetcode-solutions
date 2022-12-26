# Link: https://leetcode.com/problems/implement-trie-prefix-tree/

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Time Complexity: O(N) for all operations
# Space Complexity: O(N) for insert, O(1) for search and startsWith
# (Trie)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        tmp = self.root
        
        for x in word:
            if x not in tmp.children:
                tmp.children[x] = TrieNode()
            tmp = tmp.children[x]
            
        tmp.isWord = True

    def search(self, word: str) -> bool:
        tmp = self.root
        
        for x in word:
            if x not in tmp.children:
                return False
            tmp = tmp.children[x]
            
        return tmp.isWord

    def startsWith(self, prefix: str) -> bool:
        tmp = self.root
        
        for x in prefix:
            if x not in tmp.children:
                return False
            tmp = tmp.children[x]
        
        return True