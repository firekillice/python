#!/usr/bin/python
#coding=utf8

class actor:
	sex = 1
	desc = 'this is a test actor'

	__name = 'nobody'

	def __init__(self,name):
		self.__name = name
	
	def __test_private_func(self):
		print self.sex, self.desc, self.__name
	
	def outout_attr(self):
		self.__test_private_func()

###############################################################################
class player(actor):
	intel = 0
	strength = 0
	def __init__(self,name,intel,strength):
		actor.__init__(self,name)
		self.intel = intel
		self.strength = strength
	
	def output_attr(self):
		print self.sex,self.desc,self.intel,self.strength

###############################################################################
if __name__ == "__main__":
	actor1 = actor('Lucy')
	actor1.outout_attr()

	player1 = player('Tom',30,40)
	player1.output_attr()

###############################################################################
#1. __method can not be inherited
#2. __var can not be inherited
