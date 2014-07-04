#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os

#convert one csv table to tuple array

class tablereader:
	__filename = ''

	def __init__(self,filename):
		self.__filename = filename
		self.__open__()

	def __open__(self):
	#	print self.__filename
		f = open(self.__filename)
		lines = f.readlines()
		f.close()
		
	#	print len(lines)
		self.__content = [[]for i in range(len(lines))]
		rdindex = 0
		for line in lines:
			line=line.strip('\n')			# remove "\n"
			line=line.strip('\r')			# remove "\n"
			parts = line.split('\t')
			for index in range(0,len(parts)):
				self.__content[rdindex].append(parts[index])
			rdindex += 1
	
	def get_content(self):
		return self.__content

if __name__ == "__main__":
	_tablerder = tablereader('./equip_strengthen.csv')
	_table = _tablerder.get_content()
	for i in range(_table.__len__()):
		for j in range(_table[i].__len__()):
			print _table[i][j]
