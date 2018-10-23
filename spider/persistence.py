#!/usr/bin/python
#coding=utf8
import os,sys
import typesize

class persistence:
  def __init__(self,picpath,docpath,vopath,urlpath,datapath):
    self.__picturepath = picpath
    self.__docpath = docpath
    self.__videopath = vopath
    self.__urlpath = urlpath
    self.__datapath = datapath
    if not os.path.exists(self.__picturepath):
      os.mkdir(self.__picturepath)
    if not os.path.exists(self.__docpath):
      os.mkdir(self.__docpath)
    if not os.path.exists(self.__videopath):
      os.mkdir(self.__videopath)
    if not os.path.exists(self.__urlpath):
      os.mkdir(self.__urlpath)
    if not os.path.exists(self.__datapath):
      os.mkdir(self.__datapath)
      
  def getpicpath(self):
    return self.__picturepath
  def getdocpath(self):
    return self.__docpath
  def getvideopath(self):
    return self.__videopath
  def geturlpath(self):
    return self.__urlpath
  def getdatapath(self):
    return self.__datapath

  def afterPersistance(self,filename):
    typename, width, length = typesize.size(filename)
    #print typename,width,length
    if width < 200 or length < 200 or typename != 'JPEG':
      os.remove(filename)
      print 'remove' ,filename,width,length,typename
