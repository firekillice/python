#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os
import config

##############################################################################
class tablebase:
	filename__ = ''
	def __init__(self,filename):
		self.filename__ = filename

##############################################################################
class talblereader(tablebase):
	def __init__(self,filename):
		tablebase.__init__(self,filename)
		self.__read__()

	def __read__(self):
		f = open(self.filename__,'r')
		self.__rdlines = f.readlines()
		f.close()

	def alllines(self):
		return self.__rdlines
##############################################################################
class talblewriter(tablebase):
	def __init__(self,filename):
		tablebase.__init__(self,filename)

	def writelines(self,lines):
		f = open(self.filename__,'w')
		f.writelines(lines)
		f.close()

	def write(self,strdata):
		f = open(self.filename__,'w')
		f.write(strdata)
		f.close()

	def writedic(self,dic):
		f = open(self.filename__,'w')
		for key,value in dic.iteritems():
			f.write(value)
		f.close()

	def equal(self,reader):
		f = open(self.filename__,'w')
		#f = open(self.filename__,'a')
		f.writelines(reader.alllines())
		f.close()
#############################################################################
if __name__ == "__main__":
	_tablereader = talblereader(config.g_input_file_name)
	_tablewriter = talblewriter(config.g_output_file_name)
	_tablewriter.equal(_tablereader)
