#!/usr/bin/python
#coding=utf8

import numpy as np
from numpy import *
import config
import matplotlib.pyplot as plt

import matplotlib.font_manager as fontManager

class Plotor:
	def __init__(self):
		self.__xlabel = "xlabel"				#X轴的标签
		self.__ylabel = "ylabel"				#Y轴的标签
		self.__title = "title"					#图的标题
		self.__y_down_edge = 1					#Y轴上边界
		self.__y_up_edge = 10   				#Y轴下边界
		self.__x_left_edge = 0					#X轴左边界
		self.__x_right_edge = 10  				#X轴右边界
		self.__figure_width = 10
		self.__figure_height = 8

		self.__xy_label = "xylabel"
		self.__xz_label = "xzlabel"

		self.__xy_color = "red"
		self.__xy_linewidth = 3

	def customize_pic(self,figwidth,fighigh,title,xlabel,ylabel,xleft,xright,ydown,yup,xylabel,xzlabel):
		self.__figure_width = figwidth
		self.__figure_height = fighigh
		self.__title = title
		self.__xlabel = xlabel
		self.__ylabel = ylabel
		self.__x_left_edge = xleft
		self.__x_right_edge = xright
		self.__y_down_edge = ydown
		self.__y_up_edge = yup
		self.__xy_label = xylabel
		self.__xz_label = xzlabel

	def save_path(self,filename,dpival):
		self.__savepath = filename
		self.__dpival = dpival

	def attach_xy_data(self,xarr,yarr):
		self.__init_data__()

		self.__x = array(xarr)
		self.__y = array(yarr)
		
		self.__plot_I = plt.plot(self.__x,self.__y,label=self.__xy_label,color=self.__xy_color,linestyle='dotted',linewidth=self.__xy_linewidth)
#		self.__plot_I = plt.plot(self.__x,self.__y,label=self.__xy_label,color=self.__xy_color,linestyle='solid',linewidth=self.__xy_linewidth)

		plt.savefig(self.__savepath, dpi=self.__dpival)
		plt.legend()		#显示右上角的标签信息
		plt.show()

	def attach_xyz_data(self,xarr,yarr,zarr):
		self.__init_data__()

		self.__x = array(xarr)
		self.__y = array(yarr)
		self.__z = array(zarr)
		
		self.__plot_I = plt.plot(self.__x,self.__y,label=self.__xy_label,fontproperties="SimHei",color="green",linestyle=solid,linewidth=3)
		self.__plot_II = plt.plot(self.__x,self.__z,label = self.__xz_label,color="red",linewidth=3)

		plt.savefig(self.__savepath, dpi=self.__dpival)
		plt.legend(fontproperties="SimHei")		#显示右上角的标签信息
		plt.show(fontproperties="SimHei")

	def __init_data__(self):
		plt.figure(figsize=(self.__figure_width,self.__figure_height))
		plt.rcParams["font.family"] = "SimHei"

		plt.xlabel(self.__xlabel)
		plt.ylabel(self.__ylabel)
		plt.title(self.__title)

		plt.ylim(self.__y_down_edge,self.__y_up_edge)
		plt.xlim(self.__x_left_edge,self.__x_right_edge)


if __name__ == '__main__':
	plotor = Plotor()
	
	plotor.customize_pic(config.figWidth,config.figHeight,config.title,config.xlabel,config.ylabel,1,2,1,2,config.xydesc,'')
	plotor.save_path(config.export_fig_path,120)
	plotor.attach_xy_data([0,1],[2,3])	





