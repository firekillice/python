create_armylist_table = """
CREATE TABLE `armylist` (
  `armyid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `armyname` char(18) DEFAULT '',
  `createtime` int(10) NOT NULL DEFAULT '0',
  `armyicon` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `armylevel` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `qq` bigint(20) NOT NULL DEFAULT '0',
  `notify` char(90) DEFAULT '',
  `deletetime` int(11) NOT NULL DEFAULT '0',
  UNIQUE KEY `armyid` (`armyid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

create_armymem_table = """
CREATE TABLE `armymem` (
  `armyid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `accountid` bigint(20) unsigned NOT NULL DEFAULT '0',
  `nick` char(24) DEFAULT '',
  `job` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `rolelevel` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `fighting` int(10) unsigned NOT NULL DEFAULT '0',
  `gold` int(10) unsigned NOT NULL DEFAULT '0',
  `viplevel` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `worshipnum` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `worshiptime` int(10) NOT NULL DEFAULT '0',
  `occupation` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `grade` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `logouttime` int(3) NOT NULL DEFAULT '0',
  `deletetime` int(10) NOT NULL DEFAULT '0',
  UNIQUE KEY `accountid` (`accountid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

create_hangup_table = """
CREATE TABLE `hangUp` (
  `accountid` bigint(20) NOT NULL,
  `hangType` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `hangStartTime` bigint(20) unsigned NOT NULL DEFAULT '0',
  `isAccelerate` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `accelerateStartTime` bigint(20) unsigned NOT NULL DEFAULT '0',
  `accelerateID` smallint(5) unsigned NOT NULL DEFAULT '0',
  `packOpenState` smallint(5) unsigned NOT NULL DEFAULT '63',
  `itemGrade` smallint(5) unsigned NOT NULL DEFAULT '0',
  KEY `NewIndex1` (`accountid`,`hangType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

update_game_account_table = """
ALTER TABLE `game_account` ADD armyid BIGINT(20) UNSIGNED NOT NULL DEFAULT 0;
ALTER TABLE `game_account` ADD quitarmytime INT(10) NOT NULL DEFAULT 0;
"""


get_new_user_sql = '''
SELECT COUNT(1) FROM login_account,account_info 
WHERE login_account.createtime >= '2014-11-22 00:00:00' AND login_account.createtime <= '2014-11-22 15:00:00' 
AND account_info.accountid = login_account.accountid AND account_info.gamechannelname = '%s'
                    '''

get_new_user_sql_back = '''
SELECT COUNT(1) FROM account_info 
WHERE firstlogintime >= 1416585600 AND firstlogintime <= 1416639600 and gamechannelname = '%s'
'''

get_all_money_sql = '''
SELECT SUM(goodscount) FROM cos_account_243.order_notes 
WHERE createtime >= '2014-11-21 00:00:00' and createtime <= '2014-11-22 00:00:00' and orderid >= 100000 and 
accountid IN
    (SELECT accountid FROM cos_login_17292.account_info 
     where firstlogintime >= 1416499200 AND firstlogintime <= 1416585600  and gamechannelname = '%s')
 '''

get_all_recharge_user_num =  '''
SELECT COUNT(*) FROM (SELECT COUNT(1) FROM cos_account_243.order_notes 
where orderid >= 100000 and createtime >= '2014-11-21 00:00:00' and createtime <= '2014-11-22 00:00:00' and 
accountid IN 
    (SELECT accountid FROM cos_login_241.account_info 
        WHERE firstlogintime >= 1416499200 AND firstlogintime <= 1416585600 and gamechannelname = '%s') GROUP BY accountid)
    AS Newer;
'''
get_all_new_user_num =  '''
SELECT COUNT(1) FROM account_info 
WHERE firstlogintime >= 1416499200 AND firstlogintime <= 1416585600
'''
