#!/usr/bin/python

import random
from twisted.trial import unittest
from common import pointless

def SimpleSerializeTestCases():
	# 1) deep vector
	yield [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

	# 2) vector of vectors
	yield [range(10 + 1) for i in xrange(10)]

	# 3) randomized bitvector
	random.seed(0)
	v = pointless.PointlessBitvector(100)

	for i in xrange(40):
		v[random.randint(0, 100 - 1)] = 1

	yield v

	# 4) mixed vector
	yield [1.0, None, [1.0, True, False]]

	# 5) set
	yield set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

	# 6) empty set
	yield set()

	# 7) single item set
	yield set([1])

	# 8) mixed set
	yield set([0, 0.0, 1.0, 1, True])

	# 9) bitvectors
	for bv in AllBitvectorTestCases():
		yield bv

# all cases for bitvectors
def AllBitvectorTestCases():
	return [
		# case 0) all-0
		pointless.PointlessBitvector(sequence = [0] * 1000),

		# case 1) all-1
		pointless.PointlessBitvector(sequence = [1] * 1000),

		# case 2) 0-1
		pointless.PointlessBitvector(sequence = [0] * 400 + [1] * 800),

		# case 3) 1-0
		pointless.PointlessBitvector(sequence = [1] * 400 + [0] * 800),

		# case 4) less than 27 bits
		pointless.PointlessBitvector(sequence = [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1]),

		# case 5) a whole bunch of bits
		pointless.PointlessBitvector(sequence = [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1])
	]

from common import pointless

class TestSerialize(unittest.TestCase):
	def testSetSerialize(self):
		fname = 'test_serialize.map'

		for v in SimpleSerializeTestCases():
			pointless.serialize(v, fname)
			p = pointless.Pointless(fname)
			root = p.GetRoot()

			del root
			del p

class TestString(unittest.TestCase):
	def testString(self):
		fname = 'test_string.map'
		v = ['string', 'value', u'string', unichr(1000)]
		pointless.serialize(v, fname)
		p = pointless.Pointless(fname)
		v_ = p.GetRoot()
#		import StringIO
#		buffer_a = StringIO.StringIO()
#		buffer_b = StringIO.StringIO()
#		print v[3]
#		print v_[3]
		str(v)
		str(v_)
#		repr(v)
#		repr(v_)
#		print >> buffer_a, v
#		print >> buffer_b, v_
#		print buffer_a.getvalue()
#		print buffer_b.getvalue()
		#print map(ord, (v[3])),map(ord, (v_[3]))
		#print repr(v)
		#print repr(v_)
