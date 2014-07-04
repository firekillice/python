#!/usr/bin/python
# -*- coding: utf-8 -*- 

G_Log_Field={}
G_Log_Name=[]
G_Log_Field_Type={}

def init_global_config():
	#config all the filename and filename's field
	G_Log_Name.append("equip_strengthen.csv")
	G_Log_Field["equip_strengthen.csv"] = ["time","accountid","nickname","itemtype","itemid","val1","val2","val3","val4","val5"]
	
	#
	G_Log_Field_Type["accountid"] = "string"
	G_Log_Field_Type["time"] = "string"
	G_Log_Field_Type["nickname"] = "string"
	G_Log_Field_Type["accountid"] = "long"

def get_field_array(key):
	return G_Log_Field[key]

def get_all_filename():
	return G_Log_Name

def get_field_data_type(fieldname):
	if fieldname in G_Log_Field_Type:
		return G_Log_Field_Type[fieldname]
	return ''
