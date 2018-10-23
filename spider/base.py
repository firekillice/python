#!/usr/bin/python
#coding=utf8
import os,sys
import random
import socket
import urllib
import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError  
import re
import time;
import datetime;

import persistence
import config


class spider:
  def __init__(self,entrance):
    if not os.path.exists(config.outputdir):
      os.mkdir(config.outputdir)
    self.__persistence = persistence.persistence("picpath/","docpath/","videopath/","urlpath/","datapath/")
   
    self.__useset = set()
    self.__usedset = set()
    self.__allurlset = set()      # save domain all url
    self.__imgurlset = set()      # save img url

    self.__entrance = entrance
    matchresule = re.compile(r'.\w*').search(self.__entrance)
    if matchresule:
      self.__domain = matchresule.group()

    self.__access_cnt = 0
    self.__img_index = 0
    socket.setdefaulttimeout(5)

  def __check_doc(self,name):
    utf8_name = unicode(name,'utf-8')
    for typestring in config.doc_type_set:
      if (len(utf8_name) > len(typestring) and utf8_name[len(utf8_name) - len(typestring) : len(utf8_name)] == typestring):
        return typestring
    return ''

  def __check_pic(self,name):
    utf8_name = unicode(name,'utf-8')
    for typestring in config.pic_type_set:
      if (len(utf8_name) > len(typestring) and utf8_name[len(utf8_name) - len(typestring) : len(utf8_name)] == typestring):
        return typestring
    return ''

  def __write_used_url(self,url):
    file_object = open(self.__persistence.getdatapath() + 'used_url.conf','a')
    file_object.write(url + "\r\n")
    file_object.close()

  def handle_single_url(self,url):
    try:
      if url in self.__usedset:
        return
  #    print 'open',url

      #write cache
      self.__usedset.add(url)
      self.__write_used_url(url)
      
      #do req
      reqest = urllib2.Request(url,None,config.url_req_header)
      response = urllib2.urlopen(reqest,None,config.url_req_timeout)
      #time.sleep(0.5)
      urltext = response.read()

    except HTTPError,e:
      print 'Error:' + url,e.code
      if e.code == 404: ##not find
        return
      elif e.code == 403:
        return
    except URLError, e:
      print 'Reason: ', e.reason
      return
    except Exception,e:
      print Exception,e
      return
    
    #get jpg
    urlpattern = re.compile(r'http[^"\'<]*\.jpg')
    jpgurls = urlpattern.findall(urltext)
    for jpgurl in jpgurls:
       self.__img_persistance(jpgurl)

    #use relative href="/"
    urlprefix = re.compile(r'http://[^/]*').search(url).group()
    urlpattern = re.compile(r'href="/[^"\'<]*')
    hrefs = urlpattern.findall(urltext)
    for cururl in hrefs:
      if cururl.find(".aspx") < 0 and cururl.find(".js") < 0 and cururl.find(".css") < 0 and cururl.find(".jpg") < 0 and cururl.find(".gif") < 0 and cururl.find('.png') < 0 and cururl.find('.ico') < 0:
          cururl = cururl.strip('href="')
          self.handle_single_url(urlprefix + cururl)

    #use absolute http
  
    urlpattern = re.compile(r'http://[^"\'<]*')
    hrefs = urlpattern.findall(urltext)
    for cururl in hrefs:
      if cururl.find(self.__domain) >= 0 and cururl.find(".aspx") < 0 and cururl.find(".js") < 0 and cururl.find(".css") < 0 and cururl.find(".jpg") < 0 and cururl.find(".gif") < 0 and cururl.find('.png') < 0 and cururl.find('.ico') < 0:
          self.handle_single_url(cururl)

    #for url in self.__useset:
    #  if url not in self.__usedset:
        #print url,len(self.__usedset)
    #    self.__usedset.add(url)
     #   print url
      #  self.handle_single_url(url)

  def __img_persistance(self,url):
    try:
      if url in self.__usedset:
        return 
      self.__usedset.add(url)

      savename = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '_' + str(self.__img_index) + '.' + self.__check_pic(url)
      rawurl = url.strip('')
      filepathname = self.__persistence.getpicpath() + savename
      url = re.sub('\\\\','',url)

      urllib.urlretrieve(url,filepathname)
      self.__persistence.afterPersistance(filepathname)

  #    print 'img',url,self.__img_index
      self.__img_index += 1
    except HTTPError,e:
      print 'Error:' + url,e.code
    except URLError, e:
      print 'Reason: ', e.reason
    except Exception,e:
      print Exception,e

  def handle_url_set(self):
    try:
      for url in self.__allurlset:
        response = urllib2.urlopen(url)
        urltext = response.read()
        imgpattern = re.compile(r'http[^"]*\.[pnje]{2,3}g\b')
        imgurls = imgpattern.findall(urltext)
        for url in imgurls:
          self.__imgurlset.add(url)
    except Exception, e:
        print Exception,e

  def load_entrance(self):
    self.handle_single_url(self.__entrance)
   # self.handle_url_set()
   # self.img_persistance()
   # for line in response.readlines():
   #   self.handle_line(entrance,line)
	

if __name__ == '__main__':
  spider_instance = spider(config.entrance)
  spider_instance.load_entrance()
