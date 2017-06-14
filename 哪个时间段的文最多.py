#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd


###写完这个以后我发现自己就是个傻子 明明可以用变量和for循环做完的简单的事我偏偏手打敲了那么多个字 啊气死我了 不过等会儿关于类型的程序可以用那个方法做。
# totalbook1.xlsx  sheet4  统计所有小说（不包含已封掉的）总共36934本，除掉九月初统计书数量不够的时间，除掉page wrong和签约显示错误的书，去掉“aaaaa”
def timetype():
    wb = xlrd.open_workbook('totalbook1.xlsx')
    sh = wb.sheet_by_index(3)
    daytime = sh.col_values(14)
    daylen = len(daytime)
    hour = [1]*24
    min = [1]*60
    sec = [1]*60
    for i in range(0,24):
        hour[i]=0
    for j in range(0,60):
        min[j]=0
    for x in range(0,60):
        sec[x]=0
    str_aa = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16",
              "17", "18", "19", "20", "21", "22", "23", "24"]
    str1 = [0]*24
    for aaa in range(0,24):
        str1[aaa]=unicode(str_aa[aaa])
    str2 = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
         "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
         "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45",
         "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60"
         ]
    str3=[0]*60
    str4=[0]*60
    for bbb in range(0,60):
        str3[bbb]=unicode(str2[bbb])
        str4[bbb]=unicode(str2[bbb])
    no_any_time = 0
    octorber_num = 0
    november_num = 0
    december_num = 0
    for day in range(0, daylen):
        if (daytime[day] != ""):
            d = daytime[day].split(":")
            if (len(d) >= 2):
                details = [d[0].decode("ascii"), d[1].decode("ascii"), d[2].decode("ascii")]

                for aa in range(0,24):

                    if(details[0]==str1[aa]):
                        hour[aa]= hour[aa] + 1

                for bb in range(0,60):

                    if(details[1]==str3[bb]):
                        min[bb]=min[bb]+1

                for cc in range(0, 60):

                    if (details[2] == str4[cc]):
                        sec[cc] = sec[cc] + 1
            else:
                no_any_time = no_any_time + 1
    print "hour"
    for a in range(0,24):
        print hour[a]
    print "分钟"
    for b in range(0,60):
        print min[b]
    print "秒"
    for c in range(0,60):
        print sec[c]
    print "错误"
    print no_any_time

timetype()
