#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os
import string
import config
import table

##############################################################################
class tablecompare:
	def __init__(self,leftfile,rightfile):
		self.__leftfile = leftfile
		self.__rightfile = rightfile
		self.__leftlines = 	table.talblereader(leftfile).alllines()
		self.__rightlines = table.talblereader(rightfile).alllines()

		self.__leftkeyset = set()
		self.__rightkeyset = set()
		self.__leftkeylineinfo = {}
		self.__rightkeylineinfo = {}

		self.__analyze_left_key_info()
		self.__analyze_right_key_info()

	#从第一行开始处理
	def __analyze_left_key_info(self):
		key = 0
		rdindex = 0
		for line in self.__leftlines:
			if rdindex >= 1:
				parts = line.split('\t')
				if len(parts) >= 1:
					key = string.atoi(parts[config.get_table_key_index()])
					self.__leftkeylineinfo[key] = line
					self.__leftkeyset.add(key)
			else:
				self.__leftkeylineinfo[config.get_table_field_key()] = line
				self.__leftkeyset.add(config.get_table_field_key())
			rdindex = rdindex + 1

	#从第一行开始处理
	def __analyze_right_key_info(self):
		key = 0
		rdindex = 0
		for line in self.__rightlines:
			if rdindex >= 1:
				parts = line.split('\t')
				if len(parts) >= 1:
					key = string.atoi(parts[config.get_table_key_index()])
					self.__rightkeylineinfo[key] = line
					self.__rightkeyset.add(key)
			else:
				self.__rightkeylineinfo[config.get_table_field_key()] = line
				self.__rightkeyset.add(config.get_table_field_key())
			rdindex = rdindex + 1

	def condition_left_join(self):
		key_table = config.get_add_update_key_conditon()
		for key in key_table:
			if self.__leftkeylineinfo.has_key(key):
				old_line_info = ''
				if self.__rightkeylineinfo.has_key(key):
					old_line_info = self.__rightkeylineinfo[key]

				self.__rightkeylineinfo[key] = self.__leftkeylineinfo[key]
				self.__rightkeyset.add(key)

				new_line_info = self.__rightkeylineinfo[key]

				self.__output_table_change_log(self.__leftfile,self.__rightfile,old_line_info,new_line_info)

		

	def condition_right_join(self):
		key_table = config.get_add_update_key_conditon()
		for i in range(len(key_table)):
			key = key_table[i]
			if key in self.__rightkeylineinfo:
				self.__leftkeylineinfo[key] = self.__rightkeylineinfo[key]
				self.__leftkeyset.add(key)

	def get_left_line_info(self):
		lineinfo = []
		keylist = list(self.__leftkeyset)
		keylist.sort(key = int)					#按照顺序进行输出
		for key in keylist:
			if key in self.__leftkeylineinfo:
				lineinfo.append(self.__leftkeylineinfo[key])

		return lineinfo

	def get_right_line_info(self):
		lineinfo = []
		keylist = list(self.__rightkeyset)
		keylist.sort(key = int)					#按照顺序进行输出
		for key in keylist:
			if key in self.__rightkeylineinfo:
				lineinfo.append(self.__rightkeylineinfo[key])

		return lineinfo

	def __output_table_change_log(self,srcfile,dstfile,oldinfo,newinfo):
		f = open(config.g_log_file_path,'a')
		oldinfo = oldinfo.strip('\n')
		oldinfo = oldinfo.strip('\r')
		newinfo = newinfo.strip('\r')
		newinfo = newinfo.strip('\n')
		print >>f,"ChangeTableInfo:\t",srcfile,"-------->",dstfile
		print >>f,oldinfo
		print >>f,"---------------------------------------------------↓↓------------------------------------------------"
		print >>f,newinfo

def clear_log_file():
	f=open(config.g_log_file_path,'w')
	f.close()

def append_log_file(strdata):
	f=open(config.g_log_file_path,'a')
	print >>f,strdata
	f.close()
#############################################################################
if __name__ == "__main__":
	clear_log_file()

	for fileindex in config.g_output_file_name:
		tablecmp = tablecompare(config.g_input_file_name,config.g_output_file_name[fileindex])
		tablecmp.condition_left_join()
		tablewrer = table.talblewriter(config.g_output_file_name[fileindex])
		tablewrer.writelines(tablecmp.get_right_line_info())
		
		if config.g_run_platform == 'WIN':
			append_log_file('\r\n')
		if config.g_run_platform == 'LINUX':
			append_log_file('\n')