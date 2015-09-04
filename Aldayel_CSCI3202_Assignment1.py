#!/usr/bin/env python

from DataStructures import *
import unittest

class TestQueuesClass(unittest.TestCase):

	def test_queuingAndDequeuing(self):
		q = Queues()
		test = ""		
		for i in range(10):
			q.queue(i)
		while not q.isEmpty():
			test += str(q.dequeue())
		self.assertEqual(test, "0123456789")
	
	def test_stack(self):
		s = Stacks()
		test = ""
		for i in range(10):
			s.push(i)
		while s.checkSize() > 0:
			test += str(s.pop())
		self.assertEqual(test, "9876543210")

	def test_adding_to_tree(self):
		print "Adding 10 numbers to the tree"
		global t 
		t = BinaryTree(0)
		t.add(1,0)
		t.add(2,0)
		t.add(3,1)
		t.add(5,1)
		t.add(4,2)
		t.add(6,2)
		t.add(7,3)
		t.add(9,3)
		t.add(8,4)
		t.printTree()

	def test_deleteing_from_tree(self):
		print "Deleteing 2 and 8 "
		t.delete(2)
		t.delete(8)
		t.printTree()

	def test_graph(self):
		g = Graph()
		for i in range(10):
			g.addVertex(i)

		for j in range(7):
   			g.addEdge(j, j+1)
			g.addEdge(j, j+2)
			g.addEdge(j, j+3)

		print "Testing graph"
		g.search(1)
		g.search(3)
		g.search(4)
		g.search(6)
		g.search(9)
	
if __name__ == '__main__':
    unittest.main()