#!/usr/bin/python
# -*- coding: utf-8 -*- 

from table import tablereader
import string
from normalPlot import Plotor
import config


class StartPlot():
	def __init__(self,filename,colindex):
		self.__filename = filename
		self.__file_column = colindex

	def plot(self):
		_tablerder = tablereader(self.__filename)
		_table = _tablerder.get_content()

		_x = []
		_y = []
		_x.append(0)
		_y.append(0)

		_max_y_value = 0
		for i in range(1,_table.__len__()):
			for j in range(_table[i].__len__()):
				if j == self.__file_column:
					_x.append(i)
					_y.append(_table[i][j])
					print _table[i][j]
					if _max_y_value < string.atoi(_table[i][j]):
						_max_y_value = string.atoi(_table[i][j])

		plotor = Plotor()
		plotor.customize_pic(config.figWidth,config.figHeight,config.title,config.xlabel,config.ylabel,1,_table.__len__(),1,_max_y_value,config.xydesc,'')
		plotor.save_path(config.export_fig_path,120)
		plotor.attach_xy_data(_x,_y)

if __name__ == '__main__':
  startplot = StartPlot(config.csvfilename,config.columnindex)
  startplot.plot()