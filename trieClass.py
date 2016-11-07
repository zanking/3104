# Your name as it is on the moodle site : Zanqing Feng
# Your email: zafe5975@colorado.edu
# Your student ID: 102077587
# On my honor as a University of Colorado student, I acknowledge that
# I did not receive any unauthorized help for this assignment.
# I understand that systems like MOSS can easily detect code plagiarism.

from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
	# Initialize some fields 
  
	def __init__(self, isRootNode):
		#The initialization below is just a suggestion.
		#Change it as you will.
		# But do not change the signature of the constructor.
		self.isRoot = isRootNode
		self.isWordEnd = False # is this node a word ending node
		self.isRoot = False # is this a root node
		self.count = 0 # frequency count
		self.next = {} # Dictionary mappng each character from a-z to the child node


	def addWord(self,w):
		assert(len(w) > 0)

		# YOUR CODE HERE
		# If you want to create helper/auxiliary functions, please do so.
		if w[0] not in self.next:
			self.next[w[0]] = MyTrieNode(False)
		if len(w) > 1:
			self.next[w[0]].addWord(w[1:])
		else:
			self.next[w[0]].isWordEnd = True
			self.next[w[0]].count += 1
			
		return

	def lookupWord(self,w):
		# Return frequency of occurrence of the word w in the trie
		# returns a number for the frequency and 0 if the word w does not occur.

		# YOUR CODE HERE
		if len(w) == 0:
			return self.count
		if w[0] not in self.next:
			return 0
		else:
			return self.next[w[0]].lookupWord(w[1:])
    
	def helper(self, w_completion, w):
		if len(w_completion) < len(w):
			if w[len(w_completion)] in self.next:
				return self.next[w[len(w_completion)]].helper(w_completion + w[len(w_completion)], w)
			else:
				return []
		else:
			res = []
			if self.isWordEnd == True:
				res.append((w_completion, self.count))
			for key in self.next.keys():
				res.extend(self.next[key].helper(w_completion + key, w))
			return res
			
	
	def autoComplete(self,w):
		#Returns possible list of autocompletions of the word w
		#Returns a list of pairs (s,j) denoting that
		#         word s occurs with frequency j

		#YOUR CODE HERE
		return self.helper("", w)
    
    
            

if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
 
    
    
     
