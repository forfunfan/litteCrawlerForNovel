#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd


###写完这个以后我发现自己就是个傻子 明明可以用变量和for循环做完的简单的事我偏偏手打敲了那么多个字 啊气死我了 不过等会儿关于类型的程序可以用那个方法做。
# totalbook1.xlsx  sheet4  统计所有小说（不包含已封掉的）总共36934本，除掉九月初统计书数量不够的时间，除掉page wrong和签约显示错误的书，去掉“aaaaa”
def timetype():
    wb = xlrd.open_workbook('222.xlsx')
    sh = wb.sheet_by_index(1)
    daytime = sh.col_values(14)
    daylen = len(daytime)
    hour = [1]*24
    min = [1]*60
    sec = [1]*60
    timeaday=24*60*60
    time=[0]*timeaday
    str1 = [u"00",u"01",u"02",u"03",u"04",u"05",u"06",u"07",u"08",u"09",u"10",u"11",u"12",u"13",u"14",u"15",u"16",
              u"17",u"18",u"19",u"20",u"21",u"22",u"23",u"24"]


    str2 = [u"00",u"01",u"02",u"03",u"04",u"05",u"06",u"07",u"08",u"09",u"10",u"11",u"12",u"13",u"14",u"15",
         u"16",u"17",u"18",u"19",u"20",u"21",u"22",u"23",u"24",u"25",u"26",u"27",u"28",u"29",u"30",
         u"31",u"32",u"33",u"34",u"35",u"36",u"37",u"38",u"39",u"40",u"41",u"42",u"43",u"44",u"45",
         u"46",u"47",u"48",u"49",u"50",u"51",u"52",u"53",u"54",u"55",u"56",u"57",u"58",u"59",u"60"
         ]

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


                        for bb in range(0,60):

                            if(details[1]==str2[bb]):


                                for cc in range(0, 60):

                                    if (details[2] == str2[cc]):

                                        x=aa*60*60+bb*60+cc
                                        time[x]=time[x]+1
            else:
                no_any_time = no_any_time + 1

    for c in range(0,timeaday):
        print time[c]
    print "错误"
    print no_any_time

timetype()
