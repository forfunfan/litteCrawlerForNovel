#!/usr/bin/python
# -*- coding: UTF-8 -*-
import bs4
import re  
import requests
import urllib2
import MySQLdb
import chardet
from pyExcelerator import *
import sys
reload(sys) 
sys.setdefaultencoding('gb2312') 


def get_novel():
	root_url = 'http://www.jjwxc.net/bookbase.php?fw0=0&fbsj=3&ycx0=0&xx0=0&sd0=0&lx0=0&fg0=0&collectiontypes=ors&null=0&searchkeywords='
	#for i in (1,430)
	index_url = root_url + '&page=2';
	response = requests.get(index_url)
	response.encoding = 'gb2312'
	soup = bs4.BeautifulSoup(response.text,"html5lib").encode("gb2312")
	print soup
	
def get_novel_info():

	root_url = 'http://www.jjwxc.net/bookbase.php?fw0=0&fbsj=3&ycx0=0&xx0=0&sd0=0&lx0=0&fg0=0&collectiontypes=ors&null=0&searchkeywords='
	#for i in range(1,432)：
	index_url = root_url + '&page=2';
	response = requests.get(index_url)
	response.encoding = 'gb2312'
	soup = bs4.BeautifulSoup(response.text,"html5lib").encode("gb2312")
	index3 =0
	restotal_tr = r'<table.*?class="cytable".*?>(.*?)</table>'  
	total_tr =  re.findall(restotal_tr,soup,re.S|re.M)  
	w = Workbook()  
	ws = w.add_sheet('testnovel1')  
	for restotal in total_tr:   
		#print booktype
		booktype_tr = r'<tr.*?<td.*?<td.*?<td.*?>(.*?)</td>.*?</tr>'
		booktypetotal_tr= re.findall(booktype_tr,restotal,re.S|re.M)  									
		#for m in range(1,101):
		for a in range(1,101):		
			aaa=booktypetotal_tr[a].decode('gb2312')
			#ws.write(index3,3,booktypetotal_tr[a])
			ws.write(index3,3,aaa)
			index3=index3+1
				
		w.save('testnovel1.xls')  
		
				
	
get_novel_info()


