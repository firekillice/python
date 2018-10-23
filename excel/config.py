#!/usr/bin/python
# -*- coding: utf-8 -*- 


#信息更新方向： g_input_file_name----->g_output_file_name
g_input_file_name = "E:/phoneopen/MobileServer/bin/ZoneServer/data/activity/activityinfo.txt"

g_output_file_name = {}
g_output_file_name[1] = "E:/cos/9.5/321activity/1/activityinfo.txt";
g_output_file_name[2] = "E:/cos/9.5/321activity/2/activityinfo.txt";
g_output_file_name[3] = "E:/cos/9.5/321activity/3/activityinfo.txt";
g_output_file_name[4] = "E:/cos/9.5/321activity/4/activityinfo.txt";
g_output_file_name[5] = "E:/cos/9.5/321activity/5/activityinfo.txt";


#需要配置的key的数组
def get_add_update_key_conditon():
	return [1421,1422,1423,1424,1425,1426,1427,1428,1431,1432,1433,1434,1435,1436,1437,1441,1442,1443,1444,1445,1446,1552,1553,1554,1555,1556,1557,1558,1559,1560,1561,1562,1563,1564,1565,1566,1567,1568,1569,1570,1571,1572,1573,1574,1575,1576,1577,1578,1579,1580,1581,1582,1583];

g_log_file_path = "./changeinfo.log"

g_run_platform = 'WIN' #'LINUX'
	
#以下的内容，很少用到，暂时不用处理
######################################################################
#根据需要进行开发，暂未开发
'''def get_del_key_conditon():
	return [-1];
'''

#表中哪一列是key所在的位置
def get_table_key_index():
	return 0

	
#表中字段名的key
def get_table_field_key():
	return -1
######################################################################