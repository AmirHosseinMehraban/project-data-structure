
from operator import truediv


class TrieNode:
	
	def __init__(self):
		self.children = [None]*26

		# isEndOfWord is True if node represent the end of the word
		self.isEndOfWord = False

class Trie:
	
	# Trie data structure class
	def __init__(self):
		self.root = self.getNode()

	def getNode(self):
	
		# Returns new trie node (initialized to NULLs)
		return TrieNode()

	def _charToIndex(self,ch):
		
		# private helper function
		# Converts key current character into index
		# use only 'a' through 'z' and lower case
		
		return ord(ch)-ord('a')


	def insert(self,key):
		bad=['1','2','3','4','5','6','7','8','9','0']
		pCrawl = self.root
		length = len(key)
		for level in range(length):
			if key[level] in bad:
				return False
			index = self._charToIndex(key[level])

			# if current character is not present
			if not pCrawl.children[index]:
				pCrawl.children[index] = self.getNode()
			pCrawl = pCrawl.children[index]
		
		# mark last node as leaf
		pCrawl.isEndOfWord = True

		return True
	def search(self, key):
		pCrawl = self.root
		length = len(key)
		for level in range(length):
			index = self._charToIndex(key[level])
			if not pCrawl.children[index]:
				return False
			pCrawl = pCrawl.children[index]

		return pCrawl.isEndOfWord
	def delete(self,key):
		queue=[]
		pCrawl=self.root
		prev=self.root
		length=len(key)
		for level in range(length):
			index=self._charToIndex(key[level])
			if not pCrawl.children[index]:
				return
			if pCrawl.isEndOfWord:
				queue.append([pCrawl,level])
                  
			pCrawl=pCrawl.children[index]
              
		if pCrawl.isEndOfWord == False:
			return
            
        ##If is a prefix of another tree, just change leaf
		flag=False
        
		for i in range(26):
			if pCrawl.children[index]:
				flag=True
                
		if flag:
			pCrawl.isEndOfWord==False
			return
        ##If not a prefix but a tree longer than others, delete until isEndOfWord == True again/reach root(a unique trie)
		if len(queue)==0:
			index=self._charToIndex(key[0])
			self.root.children[index]=None
			return
		pCrawl,level=queue.pop()
		index=self._charToIndex(key[level])
		pCrawl.children[index]=None

	def load(self):
		fp = open("amir.txt",'r')
		lines=fp.readlines()
		for i in range(len(lines)):
			x=lines[i]   
			y=x.find("\n")
			x=x[0:y]
			self.insert(x)
		fp.close()   
	# Input keys (use only 'a' through 'z' and lower case)
	def am(self):
		return self.root.children
keys = ["the","a","there","anaswe","any",
		"by","their"]

	# Trie object
t = Trie()

	# Construct trie
for key in keys:
	t.insert(key)
	# Search for different keys

t.insert("dj")
t.load()