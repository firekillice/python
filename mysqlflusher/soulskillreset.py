#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os
import table

fighter_soul_skill_file = './config/fighter-soul-skill.csv'

class SkillSoulDataReset():
	def __init__(self,dbname,sqlaccess):
		try:
			self.__dbname = dbname
			self.__sqlaccess = sqlaccess
		except Exception,e:
			print Exception,e

	def __get_fighter_soul_skill_info(self):
		if not os.path.isfile(fighter_soul_skill_file):
			print 'The config file is not existed'
			return False

		self.__minorSoulSkill = {}
		self.__majorSoulSkill = {}
		self.__allMajorSoulSkill = []

		skillinfo = table.tablereader(fighter_soul_skill_file).get_content()
		for i in range(1,skillinfo.__len__()):
			_fighter_type = int(skillinfo[i][0])
			self.__minorSoulSkill[_fighter_type] = []
			self.__minorSoulSkill[_fighter_type].append(int(skillinfo[i][2]))
			self.__minorSoulSkill[_fighter_type].append(int(skillinfo[i][3]))
			self.__minorSoulSkill[_fighter_type].append(int(skillinfo[i][4]))

			self.__majorSoulSkill[_fighter_type] = int(skillinfo[i][5])
			self.__allMajorSoulSkill.append(int(skillinfo[i][5]))
	#		print self.__majorSoulSkill[_fighter_type],self.__minorSoulSkill[_fighter_type]
	
		return True

	def run(self):
		if not self.__get_fighter_soul_skill_info():
			return

		excute_sql =  "update skills set inUse = 1"
		update_result = self.__sqlaccess.update_data(self.__dbname,excute_sql)
		print "Update Skill Use Flag",update_result

		for skillid in self.__allMajorSoulSkill:
			excute_sql =  "select accountid,zonetype from skills where skillid = %s"%(skillid)
			_skill_select_result = self.__sqlaccess.select_sql(self.__dbname,excute_sql)
			print "try reset",skillid
			for result in _skill_select_result:
				_accountid = result[0]
				_zonetype = result[1]
				excute_sql =  "update skills set inUse = 0 where accountid = %s and zonetype = %s and (skillid = %s or skillid = %s or skillid = %s)"%(_accountid,_zonetype,self.__minorSoulSkill[_zonetype][0],self.__minorSoulSkill[_zonetype][1],self.__minorSoulSkill[_zonetype][2])
				update_result = self.__sqlaccess.update_data(self.__dbname,excute_sql)

				excute_sql =  "update skills set inUse = 1 where accountid = %s and zonetype = %s and skillid = %s"%(_accountid,_zonetype,skillid)
				update_result = self.__sqlaccess.update_data(self.__dbname,excute_sql)
				
				print "update skill ",_accountid,_zonetype,skillid
