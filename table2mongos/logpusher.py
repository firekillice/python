#!/usr/bin/python
#coding=utf8
import json
from module import *
from collections import OrderedDict 
import config

G_Mongo = mongo.mongoobj("192.168.1.4",27017,"logtest","root","123456")

def insert_mongo_db(filename,jsonstring):
	filenameparts=filename.split('.')
	filefirstname=filenameparts[0]
	try:
		print jsonstring
		jsonobj = json.loads(jsonstring,encoding="utf-8")
		G_Mongo.insert_json(filefirstname,jsonobj)
	except Exception, e:
		print Exception,":",e

def log_row_handle(content,fields):
	json_string = '{'
	for i in range(len(fields)):
		json_string += "\""
		json_string += fields[i]
		json_string += "\""
		json_string += ":"
		if config.get_field_data_type(fields[i]) == "string":
			json_string += "\""
		json_string += content[i]
		if config.get_field_data_type(fields[i]) == "string":
			json_string += "\""
		
		if i != len(fields) - 1:
			json_string += ","
		else:
			json_string += "}"
	return json_string

def log_file_handle(filepath,filename):
	logreader = table.tablereader(filepath)
	logcontent = logreader.get_content()
	fields = config.get_field_array(filename)
	for i in range(len(logcontent)):
		json_string=log_row_handle(logcontent[i],fields)
		insert_mongo_db(filename,json_string)

def log_dir_handle(path): 
	filenamearr = config.get_all_filename()
	for i in range(filenamearr.__len__()):
		logpath=path+filenamearr[i]
		log_file_handle(logpath,filenamearr[i])

if __name__ == "__main__":
	config.init_global_config()
	log_dir_handle("./")
