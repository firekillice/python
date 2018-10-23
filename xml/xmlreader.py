#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os
import config
from xml.dom import minidom , Node
import chardet
import re

class xmlParser:
	def __init__(self,xmlfile):
		self.__xmlfile = xmlfile
		self.__fileformat = self.__check_xml_encode__()
		self.__try_convert_to_utf8__()
	
		try:
			self.__xmldoc = minidom.parse(xmlfile)
		except Exception,e:
			self.__prepare_data__()
			self.__xmldoc = minidom.parse(xmlfile)
		#self.__parse_node__(self.__xmldoc)
		#self.__root = self.__xmldoc.documentElement

	def __prepare_data__(self):
		f = open(self.__xmlfile,"rt")
		filestream = f.read()
		f.close()

		f = open(self.__xmlfile,"w")
		f.write(config.g_file_head_append)
		f.write(filestream)
		f.write(config.g_file_tail_append)
		f.close()
		
	def __check_xml_encode__(self):
		f = open(self.__xmlfile,'rb') 
		line = f.readline()
		enc = chardet.detect(line) 
		typestring = enc['encoding'] 
		f.close() 
		return typestring

	def __try_convert_to_utf8__(self):
		if self.__fileformat != 'utf8':
			filestream = open(self.__xmlfile,"rt").read().decode(self.__fileformat,"ignore").encode("utf8")
			open(self.__xmlfile,"w").write(filestream)

	def __replace_node__(self,treenode,matchAttrValue,matchNodeValue):
		for child in treenode.childNodes:
		    if child.nodeType == Node.ELEMENT_NODE:
		    	if child.tagName == config.g_match_tag_string and child.getAttribute(config.g_match_xml_attr_key) == matchAttrValue:
		    		treenode.replaceChild(matchNodeValue,child)
		    		break
		        self.__replace_node__(child,matchAttrValue,matchNodeValue)

	def replace_xml_key_value(self,treenode,matchAttrValue,matchNodeValue):
		self.__replace_node__(self.__xmldoc,matchAttrValue,matchNodeValue)

	def __write_node_info__(self,filedec,treenode):
		for child in treenode.childNodes:
			if child.nodeType == Node.ELEMENT_NODE:
				if child.tagName == config.g_match_tag_string:
					#child.writexml(filedec)
					filedec.write(child.toxml())
				self.__write_node_info__(filedec,child)

	def after_handle_xml_data(self):
		f = open(self.__xmlfile,'w')
		self.__write_node_info__(f,self.__xmldoc)
		f.close()

if __name__ == "__main__":
	for fileindex in config.g_src_file_name:
		_xmlParser = xmlParser(config.g_dst_file_name)
	
		srcxmldoc = minidom.parse(config.g_src_file_name[fileindex])
		for child in srcxmldoc.childNodes:
		    if child.nodeType == Node.ELEMENT_NODE:
		    	if child.tagName == config.g_match_tag_string:
		    		matchKeyValue = child.getAttribute(config.g_match_xml_attr_key)
		    		print 'replace node ',matchKeyValue
		       		_xmlParser.replace_xml_key_value(child,matchKeyValue,child)
		       		break

		_xmlParser.after_handle_xml_data()