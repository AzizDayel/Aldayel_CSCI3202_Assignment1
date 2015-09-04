#!/usr/bin/env python

import Queue

class Queues:
	def __init__(self):
		self.q = Queue.Queue()

	def queue (self,x):
		if type(x) is int:
			self.q.put(x)
		else:
			print "This queue only accept int"
		return

	def dequeue(self):
		return self.q.get()
	
	def isEmpty(self):
		return self.q.empty()

class Stacks:
	
	def __init__(self):
        	self.s = []

	def push(self, x):
		if type(x) is int:
			self.s.append(x)
		else:
			print "This stack only accept int"
		return
	
	def pop(self):
		return self.s.pop()

	def checkSize(self):
		return len(self.s)

class Node():

	def __init__(self, key, parent):
		self.left = None
		self.right = None
		self.parent = parent
		self.key = key

	def setLeft(self, node):
		self.left = node 
	
	def setRight(self, node):
		self.right = node
	
	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def getParent(self):
		return self.parent
	
	def getKey(self):
		return self.key

class BinaryTree():
	
	def __init__(self, key):
		self.node = Node(key, None)
	
	# search the tree for a certain value
	def search (self, initNode, value):
		if (initNode.getKey() == value):
			return initNode 
		else:
			if (initNode.getLeft() is not None):
				Fnode = self.search(initNode.getLeft(), value)
				if Fnode is not None:
					return Fnode
			if (initNode.getRight() is not None):
				Fnode = self.search(initNode.getRight(), value)				
				if Fnode is not None:
					return Fnode

	def add(self, value, parentValue): 
		parentNode = self.search( self.node, parentValue)
		if parentNode is None:
			print "Parent not found."		
		elif parentNode.getLeft() is None:
			parentNode.setLeft( Node(value, parentNode) )
		elif parentNode.getRight() is None:
			parentNode.setRight( Node(value, parentNode) )
		else:
			print "Parent has two children, node not added."

	def delete(self, value):
		dNode = self.search( self.node, value)
		if dNode is None:
			print "Node %d not found." %value
		elif (dNode.getLeft() is None) and (dNode.getRight() is None):
			dNode = dNode.getParent()
			if (( dNode.getLeft() ).getKey() == value ):
				dNode.setLeft(None)
			else:
				dNode.setRight(None)
		else:
			print "Node %d not deleted, has children.\n" %value

	def printTree(self):
		self.printRec(self.node)
	
	def printRec(self, currNode):
		if (currNode is None):
			return 
		else:
			parentNode = currNode.getParent()
			print "Node ",currNode.getKey()
			if parentNode is None:
				print " parent None"
			else:
				print " parent", parentNode.getKey()
			self.printRec(currNode.getLeft())
			self.printRec(currNode.getRight())

class Graph():
	def __init__(self):
		self.dictionary = {}
    
	def addVertex(self, value):
		if (self.dictionary).has_key(value):
			print "Vertex already exists"
		else:
			self.dictionary[value] = []
    
	def addEdge(self, value1, value2):
		if not (self.dictionary.has_key(value1) and self.dictionary.has_key(value2)):
			print "One or more vertices not found"
		else:
			self.dictionary[value1].append(value2)
			self.dictionary[value2].append(value1)
    
	def search(self, value):
		if (self.dictionary.has_key(value)):
			print ("Adjacent vertices for key %i" % value)
			for i in self.dictionary[value]:
				print i
