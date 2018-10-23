#!/usr/bin/python
# -*- coding: utf-8 -*- 


#信息更新方向： g_src_file_name----->g_dst_file_name
g_src_file_name = {}
g_src_file_name[1] = "./ui_resource11.xml"
g_src_file_name[2] = "./ui_resource11.xml"
g_dst_file_name = './ui_resource.xml'


g_match_tag_string = 'TextureAtlas'
g_match_xml_attr_key = 'imagePath'

####此处是为了调整xml的文件信息而是用的，因为目标文件不是标准的xml文件，没有root
g_file_head_append = '<append_string>'
g_file_tail_append = '</append_string>'

g_xml_mark_string = '<?xml version="1.0" ?>'