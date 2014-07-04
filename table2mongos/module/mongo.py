#!/usr/bin/python 
# -*- coding: utf-8 -*- 
import os
import pymongo
import random
from bson.objectid import ObjectId  

class mongoobj:
	def __init__(self,ip,port,dbname,user,pw):
		try:
			self.__client = pymongo.MongoClient(ip,port)
			self.__db = self.__client['admin']		#through admin auth
			self.__db.authenticate(user,pw)

			#get smooth env
			self.__db = self.__client[dbname]
		except Exception, e:
			print Exception,":",e 

	def get_collection_names(self):
		print self.__db.collection_names()

	def insert_json(self,collection,jsondata):
		try:
			collection_name = self.__db[collection]
			collection_name.insert(jsondata) 
		except Exception, e:
			print Exception,":",e
	
	def show_collection(self,collname):
		print collname,self.__db[collname].find().count()
		for item in self.__db[collname].find():
			print item



if __name__ == "__main__":
	_mongoobj = mongoobj("192.168.1.4",27017,'logtest','root','123456')
	_mongoobj.insert_json('python_test',{'id':2, 'name':'hello'})
	#_mongoobj.show_collection("equip_strengthen")
