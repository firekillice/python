#!/usr/bin/python
# -*- coding: utf-8 -*-

import gamemysql
import soulskillreset
import config.dbconfig as dbconfig
from config.channel import channel as channel

#host related
db_host = '192.168.1.47'
#db_host = '10.66.100.83'
db_port = 3306
#db_user = 'linghegu17292'
db_user = 'mysql'
#db_user = 'slaveroot'
db_passwd = '1'
#db_passwd = 'U5Lk*f7n7K'
Gamesql = gamemysql.GameMysql(db_host,db_port,db_user,db_passwd)

#database name
excute_db_name = ['cos_login_156']
excute_affair_name = ['wb_test_cos_affair']

#插入一个新的字段和魔神的初始化信息
def excute_flush_data():
	for dbname in excute_db_name:
		_excute_sql =  "select accountid from game_account"

		print _excute_sql,dbname
		_account_result = Gamesql.select_sql(dbname,_excute_sql)

		_insert_data = []
		for r in _account_result:
			_accountid = r[0]
			_insert_data.append((_accountid,12,0,0,0,0,0))

		_insert_sql = 'insert into demon values(%s,%s,%s,%s,%s,%s,%s)'
		Gamesql.insert_more(dbname,_insert_sql,_insert_data)

		print _accountid

#清理任务和排行榜的历史信息
def clear_db_data():
	for dbname in excute_db_name:
		print "operating",dbname

		_excute_sql =  "truncate %s"%("demon")
		_account_result = Gamesql.del_data(dbname,_excute_sql)

		_excute_sql =  "delete from  %s where taskid >= 4118 and taskid <= 4130 "%("runtask")
		_account_result = Gamesql.del_data(dbname,_excute_sql)

	for dbname in excute_affair_name:
		print "operating",dbname
		_excute_sql =  "truncate %s"%("demondata")
		_account_result = Gamesql.del_data(dbname,_excute_sql)

		_excute_sql =  "delete from  %s where billboardtypeid >= 2000 and billboardtypeid <= 2001 "%("billboard_info")
		_account_result = Gamesql.del_data(dbname,_excute_sql)

# 更新每月登陆
def update_db_data():
	for dbname in excute_db_name:
		print "operating",dbname
		#_excute_sql =  "update game_account set vipbuyinfo = 0"
		_excute_sql =  "update game_account set monthlogininfo = 0"
		_account_result = Gamesql.update_data(dbname,_excute_sql)

#命魂玩法的修改
def reset_soul_skill_data():
	for dbname in excute_db_name:
		print "operating ",dbname
		_soulskillreset = soulskillreset.SkillSoulDataReset(dbname,Gamesql)
		_soulskillreset.run()

#更新军团和挂机的表结构
def updateDataTable():
	for dbname in excute_db_name:
		Gamesql.create_table(dbname,dbconfig.create_hangup_table)
		Gamesql.alert_table(dbname,dbconfig.update_game_account_table)
	
	for dbname in excute_affair_name:
		Gamesql.create_table(dbname,dbconfig.create_armylist_table)
		Gamesql.create_table(dbname,dbconfig.create_armymem_table)

#获得新用户的个数
def get_new_user():
    for dbname in excute_db_name:
        for channelname in channel:
			_excute_sql =  dbconfig.get_new_user_sql%(channelname)
			account_result = Gamesql.select_sql(dbname,_excute_sql)
			for r in account_result:
				user_number = r[0]
				print channelname,'\t',user_number

#获得充值的总额
def get_all_money():
	for channelname in channel:
		_excute_sql =  dbconfig.get_all_money_sql%(channelname)
		account_result = Gamesql.select_sql_up_db(_excute_sql)
		for r in account_result:
			money_number = r[0]
			print channelname,'\t',money_number

#获得用户中充值的人数
def get_all_rechareg_user_num():
	for channelname in channel:
		_excute_sql =  dbconfig.get_all_recharge_user_num%(channelname)
		account_result = Gamesql.select_sql_up_db(_excute_sql)
		for r in account_result:
			money_number = r[0]
			print channelname,'\t',money_number

#获得新用户的个数
def get_all_new_user():
    	for dbname in excute_db_name:
		_excute_sql =  dbconfig.get_all_new_user_num
        account_result = Gamesql.select_sql(dbname,_excute_sql)
		print _excute_sql
		for r in account_result:
			user_number = r[0]
			print user_number
if __name__ == "__main__":
	get_new_user()
