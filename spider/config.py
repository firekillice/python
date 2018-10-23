#!/usr/bin/python
#coding=utf8

#定义网址的入口
entrance='http://image.baidu.com/'
#定义输出的信息的路径
outputdir='./resources/'

#请求的一些配置信息
url_req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
'Accept-Charset':'utf-8;',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Connection':'close'
#'Host':'images.mafengwo.net'
}
url_req_timeout = 5

#定义需要判定的文件类型的集合
pic_type_set = ["jpeg",'jpg','png','bmp','gif']
doc_type_set = ["txt",'doc','docx','pdf','ppt','pptx']
#######################################################################
