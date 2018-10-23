#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import MySQLdb
import MySQLdb.cursors

class GameMysql():
	def __init__(self,host,port,user,pwd):
		try:
			print host,port,user,pwd
			self.__conn = MySQLdb.connect(host = host,port = port,user = user,passwd = pwd)
			self.__cursor = self.__conn.cursor()
		except Exception,e:
			print Exception,e

	def try_create_db(self,dbname):
		self.__cursor.execute('create database if not exists ' + dbname)

	def clear_table(self,dbname,tablename):
		try:
			self.__before_excute__(dbname)
			return self.__cursor.execute("truncate %s"%(dbname))
		except Exception,e:
			print Exception,e

	def check_table(self,dbname,tablename):
		self.__before_excute__(dbname)
		exe_sql = "show tables like '%s'" %(tablename)
		self.__cursor.execute(exe_sql)

		result = self.__cursor.fetchone()
		if result:
	   		 return True
		else:
			return False

	
	def create_table(self,dbname,createsql):
		try:
			self.__before_excute__(dbname)
			return self.__cursor.execute(createsql)
		except Exception,e:
			print Exception,e
			
	def alert_table(self,dbname,alertsql):
		try:
			self.__before_excute__(dbname)
			return self.__cursor.execute(alertsql)
		except Exception,e:
			print Exception,e
	
	def __before_excute__(self,dbname):
		self.__conn.select_db(dbname)

	#insert table
	def select_sql(self,dbname,mysql):
		try:
			self.__before_excute__(dbname)
			count = self.__cursor.execute(mysql)
			results=self.__cursor.fetchall()
			return results
		except Exception,e:
			print Exception,e

	#select data beyond db
	def select_sql_up_db(self,mysql):
		try:
			count = self.__cursor.execute(mysql)
			results=self.__cursor.fetchall()
			return results
		except Exception,e:
			print Exception,e

	#insert table
	def insert_more(self,dbname,mysql,data):
		try:
			self.__before_excute__(dbname)
			self.__cursor.executemany(mysql,data)
			self.__conn.commit()
		except Exception,e:
			print Exception,e

	def del_data(self,dbname,mysql):
		try:
			self.__before_excute__(dbname)
			self.__cursor.execute(mysql)
			self.__conn.commit()
		except Exception,e:
			print Exception,e

	def update_data(self,dbname,mysql):
		try:
			self.__before_excute__(dbname)
			self.__cursor.execute(mysql)
			self.__conn.commit()
		except Exception,e:
			print Exception,e

	#close this mysql conn
	def close(self):
		self.__cursor.close()
		self.__conn.close()
