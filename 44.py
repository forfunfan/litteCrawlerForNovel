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
    # for i in (1,449)
    index_url = root_url + '&page=2';
    response = requests.get(index_url)
    response.encoding = 'gb2312'
    soup = bs4.BeautifulSoup(response.text, "html5lib").encode("gb2312")
    print soup


def get_novel_info():
    reload(sys)
    sys.setdefaultencoding('utf8')
    w = Workbook()
    ws = w.add_sheet('testnovel444')
    origin_url = 'http://www.jjwxc.net/'
    root1_url = 'http://www.jjwxc.net/bookbase.php?fw0=0&fbsj=3&ycx0=0&xx0=0&sd0=0&lx0=0&fg0=0&sortType=4&page='
    root2_url = "&isfinish=0&collectiontypes=ors&searchkeywords="
    for i in range(398, 410):
        n = bytes(i)
        index_url = root1_url + n + root2_url
        index1 = (i - 1) * 100
        index2 = (i - 1) * 100
        index3 = (i - 1) * 100
        index4 = (i - 1) * 100
        index5 = (i - 1) * 100
        index6 = (i - 1) * 100
        index7 = (i - 1) * 100
        index8 = (i - 1) * 100
        index9 = (i - 1) * 100
        index10 = (i - 1) * 100
        index11 = (i - 1) * 100
        index12 = (i - 1) * 100
        index13 = (i - 1) * 100
        index14 = (i - 1) * 100
        response = requests.get(index_url)
        response.encoding = 'gb2312'
        soup = bs4.BeautifulSoup(response.text, "html5lib").encode("gb2312")
        # content = soup.findAll(attrs={"class":"cytable"})
        # res_tr = r'<tr>.*?<td.*?<td.*?(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td></tr>'
        # ('<TR>.*?<p.*?<p.*?<p.*?<p.*?<p.*?>(.*?)</p>.*?<p.*?<p.*?>(.*?)</p>.*?</TR>'
        restotal_tr = r'<table.*?class="cytable".*?>(.*?)</table>'
        total_tr = re.findall(restotal_tr, soup, re.S | re.M)
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
                for authorurl in authortotalurls_tr:
                    ws.write(index10,10,authorurl)
                    index10=index10+1
                    intoauthorurl = origin_url + authorurl
                    response2 = requests.get(intoauthorurl)
                    response2.encoding = 'gb2312'
                    soup2 = bs4.BeautifulSoup(response2.text,"html5lib").encode("gb2312")
                    #author collected
                    authorcollected_tr=r'<td\scolspan="5".*?<img\s.*?><br/>(.*?)\n*<br/>\n.*?</td>'
                    authorcollectedtotal_state =  re.findall(authorcollected_tr,soup2,re.S|re.M)
					#author novelnum
                    authornovelnum_tr=r'<td\scolspan="5".*?<td\scolspan="2".*?>(.*?)\n*</td>\n.*?</td>'
                    authornovelnumtotal_state =  re.findall(authornovelnum_tr,soup2,re.S|re.M)
					#autorcollect
                    if authorcollectedtotal_state != []:
                        for authorcollect in authorcollectedtotal_state:
                            #authcol=authorcollect.decode('windows-1252')
                            print chardet.detect("authorcollect")
                            aucol=authorcollect.decode("gbk")
                            aucoll=aucol.split("：")[1]
                            ws.write(index12,12,aucoll)
                            index12=index12+1
                            print aucoll
                        for am in authornovelnumtotal_state:
                            str="href"
                            authornumfinal=am.count(str)
                            ws.write(index11,11,authornumfinal)
                            index11=index11+1
                    else:
                        str22="aaaaa"
                        ws.write(index12, 12, str22)
                        index12 = index12 + 1
                        ws.write(index11, 11, str22)
                        index11 = index11 + 1
            # print nameinfo
            nameinfo_tr = r'<tr.*?<td.*?<td.*?>(.*?)</td>.*?</tr>'
            nameinfototal = re.findall(nameinfo_tr, restotal, re.S | re.M)
            # print booktype
            booktype_tr = r'<tr.*?<td.*?<td.*?<td.*?>(.*?)</td>.*?</tr>'
            booktypetotal_tr = re.findall(booktype_tr, restotal, re.S | re.M)
            # print wordnumber
            wordnum_tr = r'<tr.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?>(.*?)</td>.*?</tr>'
            wordnumtotal_tr = re.findall(wordnum_tr, restotal, re.S | re.M)
            # print scores
            scores_tr = r'<tr.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?>(.*?)</td>.*?</tr>'
            scorestotal_tr = re.findall(scores_tr, restotal, re.S | re.M)
            # print time
            time_tr = r'<tr.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?>(.*?)</td>.*?</tr>'
            timetotal_tr = re.findall(time_tr, restotal, re.S | re.M)
            #print name & url
            for nameinfo in nameinfototal:
                name_tr = r'<a .*?>(.*?)</a>'
                url_tr = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
                lable_tr = r"(?<=title=\").+?(?=\")|(?<=title=\').+?(?=\')"
                nameurls_tr = re.findall(url_tr, nameinfo, re.I | re.S | re.M)
                nametotal_tr = re.findall(name_tr, nameinfo, re.S | re.M)
                labletotal_tr = re.findall(lable_tr, nameinfo, re.S | re.M)
                # print lable
                for title in labletotal_tr:
                    title1 = title.decode('gb2312')
                    title2 = title1.split("：")[2]
                    ws.write(index13, 13, title2)
                    index13 = index13 + 1
                # print book name and url
                for name in nametotal_tr:
                    boname = name.decode('gb2312')
                    ws.write(index1, 1, boname)
                    index1 = index1 + 1
                for bookurl in nameurls_tr:
                    ws.write(index2, 2, bookurl)
                    index2 = index2 + 1
                    origin_url = 'http://www.jjwxc.net/'
                    intobookurl = origin_url + bookurl
                    print bookurl
                    response1 = requests.get(intobookurl)
                    response1.encoding = 'gb2312'
                    soup1 = bs4.BeautifulSoup(response1.text, "html5lib").encode("gb2312")
                    # sign state
                    state = r'<ul.*?name="printright".*?<li.*?<li.*?<li.*?<li.*?<li.*?<li.*?<li.*?<li.*?<li.*?>(.*?)</li>.*?</ul>'
                    total_state = re.findall(state, soup1, re.S | re.M)
                    # novel collected 8
                    collected1_tr = r'<span.*?itemprop="collectedCount".*?>(.*?)</span>'
                    collected2_tr = r'<div.*?class="smallreadbody".*?<div.*?<div.*?<div.*?>(.*?)</div>.*?</div>'
                    collectedtotal1_tr = re.findall(collected1_tr, soup1, re.S | re.M)
                    collectedtotal2_tr = re.findall(collected2_tr, soup1, re.S | re.M)
                    # novel comment 9
                    comment1_tr = r'<span.*?itemprop="reviewCount".*?>(.*?)</span>'
                    comment2_tr = r'<div.*?class="smallreadbody".*?<div.*?<div.*?<div.*?>(.*?)</div>.*?</div>'
                    commenttotal1_tr = re.findall(comment1_tr, soup1, re.S | re.M)
                    commenttotal2_tr = re.findall(comment2_tr, soup1, re.S | re.M)
                    if (collectedtotal1_tr!=[] ):
                        collected_tr=collectedtotal1_tr[0]
                        ws.write(index9, 9, collected_tr)
                        index9 = index9 + 1
                    elif (collectedtotal1_tr==[] and collectedtotal2_tr!=[]):
						#collected_tr=collectedtotal2_tr[0]
                        ab = collectedtotal2_tr[0].decode("gb2312")
                        abb = ab.split("：")
                        if (len(abb) >=3):
						    collected_tr =abb[3].split(" ")[0]
						    ws.write(index9, 9, collected_tr)
						    index9 = index9 + 1
                        else:
                            collected_tr =  "page wrong"
                            ws.write(index9, 9, collected_tr)
                            index9 = index9 + 1
                    else:
						collected_tr="aaaaa"
						ws.write(index9, 9, collected_tr)
						index9 = index9 + 1

                    if (commenttotal1_tr!= []):
                        comment_tr = commenttotal1_tr[0]
                        ws.write(index8, 8,comment_tr)
                        index8 = index8 + 1
                    elif (commenttotal1_tr == [] and commenttotal2_tr != []):
                        ac = commenttotal2_tr[0].decode("gb2312")
                        acc = ac.split("：")
                        if (len(acc) >= 2):
                            collected_tr = acc[2].split(" ")[0]
                            ws.write(index8, 8, collected_tr)
                            index8 = index8 + 1
                        else:
                            comment_tr = "page wrong"
                            ws.write(index8, 8, comment_tr)
                            index8 = index8 + 1
                    else:
						comment_tr = "aaaaa"
						ws.write(index8, 8, comment_tr)
						index8 = index8 + 1
                   #sign state
                    if (total_state!=[]):
						sigh_state = r'<font .*?>(.*?)</font>'
						total_sign = re.findall(sigh_state, total_state[0], re.S | re.M)
						if (total_sign!=[]):
							bosigh = total_sign[0].decode('gb2312')
							ws.write(index7, 7, bosigh)
							index7 = index7 + 1
							print index7
						else:
							x="no any description"
							ws.write(index7,7,x)
							index7 = index7 + 1
							print index7
                    else:
                        xx = "aaaaa"
                        ws.write(index7, 7, xx)
                        index7 = index7 + 1
                        print index7
            #for m in range(1,101):
            pagenovelnumber_tr = len(booktypetotal_tr)
            for a in range(1, pagenovelnumber_tr):
                print booktypetotal_tr[a].decode('gb2312')
                botype = booktypetotal_tr[a].decode('gb2312')
                ws.write(index3, 3, botype)
                ws.write(index3, 4, wordnumtotal_tr[a])
                daytime = timetotal_tr[a]
                daytime = daytime.split(" ")
                if (daytime != ['']):
                    day = daytime[0]
                    time = daytime[1]
                    ws.write(index3, 5, day)
                    ws.write(index3, 14, time)
                    index14 = index14 + 1
                else:
                    ws.write(index3, 5, "page wrong")
                    ws.write(index3, 14, "page wrong")
                    index14 = index14 + 1
                ws.write(index3, 6, scorestotal_tr[a])
                index3 = index3 + 1
                print scorestotal_tr[a]
                w.save('testnovel444.xls')
        print i



    # 第一列小说名，第二列小说url，第三列小说类型，第四列总字数，第五列发表时间，第六列总积分，第七列签约状态，第八列收藏数，第九列总评论数
    # 第十列作者专栏url 第十一列作者小说数量，第十二列作者收藏数


get_novel_info()
