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



def get_novel():
	root_url = 'http://www.jjwxc.net/bookbase.php?fw0=0&fbsj=3&ycx0=0&xx0=0&sd0=0&lx0=0&fg0=0&collectiontypes=ors&null=0&searchkeywords='
	#for i in (1,430)
	index_url = root_url + '&page=2';
	response = requests.get(index_url)
	response.encoding = 'gb2312'
	soup = bs4.BeautifulSoup(response.text,"html5lib").encode("gb2312")
	print soup
	
def get_novel_info():
	reload(sys) 
	sys.setdefaultencoding('utf8') 
	w = Workbook()  
	ws = w.add_sheet('testnovel1')  
	origin_url = 'http://www.jjwxc.net/'
	root_url = 'http://www.jjwxc.net/bookbase.php?fw0=0&fbsj=3&ycx0=0&xx0=0&sd0=0&lx0=0&fg0=0&collectiontypes=ors&null=0&searchkeywords='
	for i in range(1,2):
		n=bytes(i)
		index_url = root_url + '&page='+n;
		index1 = (i-1)*100
		index2 = (i-1)*100
		index3 = (i-1)*100
		index4 = (i-1)*100
		index7 = (i-1)*100
		index8 = (i-1)*100
		index9 = (i-1)*100
		index10 = (i-1)*100
		response = requests.get(index_url)
		response.encoding = 'gb2312'
		soup = bs4.BeautifulSoup(response.text,"html5lib").encode("gb2312")
		#content = soup.findAll(attrs={"class":"cytable"})
		#res_tr = r'<tr>.*?<td.*?<td.*?(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td></tr>'      
		#('<TR>.*?<p.*?<p.*?<p.*?<p.*?<p.*?>(.*?)</p>.*?<p.*?<p.*?>(.*?)</p>.*?</TR>'
		restotal_tr = r'<table.*?class="cytable".*?>(.*?)</table>'  
		total_tr =  re.findall(restotal_tr,soup,re.S|re.M)  
		for restotal in total_tr:  
			#print authorinfo
			authorinfo_tr = r'<tr.*?<td.*?>(.*?)</td>.*?</tr>'
			authorinfototal_tr = re.findall(authorinfo_tr,restotal,re.S|re.M) 	
			#print author info
			for authorinfo in authorinfototal_tr:
				authorname_tr = r'<a .*?>(.*?)</a>'  
				authorurl_tr = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"  
				authortotalurls_tr = re.findall(authorurl_tr, authorinfo, re.I|re.S|re.M)
				authornametotal_tr =  re.findall(authorname_tr, authorinfo, re.S|re.M) 
				print authortotalurls_tr
				print authornametotal_tr
				for authorname in authornametotal_tr:	
					auname=authorname.decode('gb2312')
					#作者名字在第7列
					ws.write(index7,7,auname) 
					index7=index7+1
					print index7
				for authorurl in authortotalurls_tr:			
					ws.write(index8,8,authorurl) 
					index8=index8+1
					intoauthorurl = origin_url + authorurl;
					response2 = requests.get(intoauthorurl)
					response2.encoding = 'gb2312'
					soup2 = bs4.BeautifulSoup(response2.text,"html5lib").encode("gb2312")
					#author collected
					authorcollected_tr=r'<td.*?colspan="5".*?img.*?>(.*?)'
					authorcollectedtotal_state =  re.findall(authorcollected_tr,soup2,re.S|re.M)
					#novel num
					authornovelnum_tr=r'<table.*?width="760".*?border="0".*?align="center".*?cellpadding="0".*?cellspacing="0".*?<table.*?<td.*?colspan="2">(.*?)</td></table>'
					authornovelnumtotal_tr =  re.findall(authornovelnum_tr,soup2,re.S|re.M) 
			

							
		w.save('testnovel1.xls')  
	
		
				
	
get_novel_info()