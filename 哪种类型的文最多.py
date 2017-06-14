#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd


###写完这个以后我发现自己就是个傻子 明明可以用变量和for循环做完的简单的事我偏偏手打敲了那么多个字 啊气死我了 不过等会儿关于类型的程序可以用那个方法做。

def timetype():
    wb = xlrd.open_workbook('totalbook1.xlsx')
    sh = wb.sheet_by_index(3)
    daytime = sh.col_values(3)
    daylen = len(daytime)
    all_type = ["爱情","武侠", "奇幻", "仙侠","网游", "传奇",  "科幻",  "童话", "恐怖", "侦探", "动漫", "影视" ,"小说", "真人", "其他", "剧情", "轻小说"]
    type = [1]*17
    for i in range(0,17):
        type[i]=0
    no_any_time = 0
    octorber_num = 0
    november_num = 0
    december_num = 0
    for day in range(0, daylen):
        if (daytime[day] != ""):
            d = daytime[day].split("-")
            if (len(d) >= 3):


             
                details1 = [d[0].encode("utf8"), d[1].encode("utf8"), d[2].encode("utf8"),d[3].encode("utf8")]
                de =details1[3].replace(" ","")
                for aa in range(0,17):

                    if(de==all_type[aa]):
                        type[aa]= type[aa] + 1

                    else:
                        no_any_time = no_any_time + 1
            november_num= november_num+1
    for a in range(0,17):
        print type[a]

    print no_any_time
    print november_num
timetype()
