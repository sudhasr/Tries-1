"""Using disctionary"""

#Accepted on Leetcode

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.triedict = dict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
		#Time Complexity - O(1)
		#Space complexity - O(1)
        self.triedict[word] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
		#Time Complexity - O(n)
		#Space complexity - O(1)
        for i in self.triedict.keys():
            if word == i:
                return True
        return False
    
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
		#Time Complexity - O(1)
		#Space complexity - O(1)
        for i in self.triedict.keys():
            if i.startswith(prefix):
                return True
        return False
    

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)