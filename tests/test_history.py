# -*- coding: utf-8 -*-

import unittest

import history

class TestHistory(unittest.TestCase):
	def test_symple_add(self):
		hist=history.History()
		self.assertTrue(hist.isEmpty())
		hist.add(0)
		self.assertFalse(hist.isEmpty())
		hist.add(1)
		self.assertEqual(hist.getCount(),2)
		self.assertEqual(hist.get(1), 1)
		self.assertEqual(hist.getList(), [0,1])

		hist.clear()
		self.assertEqual(hist.getCount(),0)
		self.assertEqual(hist.get(1), None)
		self.assertEqual(hist.getList(), [])

	def test_overflow(self):
		hist=history.History(3)
		hist.add(0)
		hist.add(1)
		hist.add(2)
		hist.add(3)
		self.assertEqual(hist.getCount(),3)
		self.assertEqual(hist.get(1), 2)
		self.assertEqual(hist.getList(), [1,2,3])

	def test_Duplication(self):
		hist=history.History(3)
		hist.add(0)
		hist.add(1)
		hist.add(0)
		self.assertEqual(hist.getCount(),3)
		self.assertEqual(hist.getList(), [0,1,0])

		hist=history.History(3,False)
		hist.add(0)
		hist.add(1)
		hist.add(0)
		self.assertEqual(hist.getCount(),2)
		self.assertEqual(hist.getList(), [1,0])

	def test_cursor(self):
		hist=history.History(4)
		self.assertEqual(hist.getNext(),None)
		self.assertEqual(hist.getPrevious(),None)
		self.assertEqual(hist.getNext(),None)
		self.assertFalse(hist.hasPrevious())
		self.assertFalse(hist.hasNext())
		hist.add(0)
		self.assertFalse(hist.hasPrevious())
		self.assertFalse(hist.hasNext())
		self.assertEqual(hist.getNext(),None)
		self.assertEqual(hist.getPrevious(),None)
		self.assertEqual(hist.getNext(),None)
		hist.add(1)
		self.assertFalse(hist.hasNext())
		self.assertTrue(hist.hasPrevious())
		self.assertFalse(hist.hasNext())
		self.assertEqual(hist.getNext(),None)
		self.assertTrue(hist.hasPrevious())
		self.assertFalse(hist.hasNext())
		self.assertEqual(hist.getPrevious(),0)
		self.assertFalse(hist.hasPrevious())
		self.assertTrue(hist.hasNext())
		self.assertEqual(hist.getPrevious(),None)
		self.assertEqual(hist.getNext(),1)
		self.assertEqual(hist.getNext(),None)
		self.assertTrue(hist.hasPrevious())
		self.assertFalse(hist.hasNext())
		hist.add(2)
		hist.getPrevious()
		hist.add(4)
		self.assertEqual(hist.getCount(),3)
		self.assertEqual(hist.getList(), [0,1,4])
		self.assertEqual(hist.getNext(),None)
		self.assertEqual(hist.getPrevious(),1)
