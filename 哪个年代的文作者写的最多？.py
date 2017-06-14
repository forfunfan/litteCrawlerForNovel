#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd


def noveltypeofauthormost(first_column):
    wb = xlrd.open_workbook('totalbook.xlsx')
    sh= wb.sheet_by_index(0)
    first_column = sh.col_values(3)
    daytime = sh.col_values(5)

    booklen = len(first_column)
    xian_dai_jin_dai = 0
    gu_se_gu_xiang = 0
    jia_kong_li_shi = 0
    huan_xiang_wei_lai = 0
    do_not_know_error = 0
    totally_error = 0
    booktypenull = 0
    weizhi = 0
    for booktype in range(0,booklen):
            if (first_column[booktype] != ""):
                #typelist = first_column[booktype].encode('gb2312')
                typelist = first_column[booktype]
                type = typelist.split("-")
                typelen = len(type)
                # 同人和原创数量比较：
                if (typelen > 1):
                    first_type = type[2].encode('utf8')
                    if(first_type == "近代现代"):
                        xian_dai_jin_dai = xian_dai_jin_dai + 1
                    elif(first_type == "古色古香"):
                       gu_se_gu_xiang = gu_se_gu_xiang + 1
                    elif(first_type == "架空历史"):
                        jia_kong_li_shi = jia_kong_li_shi + 1
                    elif(first_type == "幻想未来"):
                        huan_xiang_wei_lai = huan_xiang_wei_lai + 1
                    else:
                        do_not_know_error = do_not_know_error +1
                        print first_type
                        if first_type == "未知":
                            weizhi = weizhi+1
                else:
                    totally_error = totally_error+1
            else:
                booktypenull = booktypenull + 1

    print "现代近代"+bytes(xian_dai_jin_dai),"古色古香"+bytes(gu_se_gu_xiang),"架空历史"+bytes(jia_kong_li_shi),"幻想未来"+bytes(huan_xiang_wei_lai)

    print "jj抽了没有类型"+bytes(booktypenull)
    print "do_not_know_errors"+bytes(do_not_know_error)
    print "未知"+bytes(weizhi)

def timetype(daytime):

    daylen = len(daytime)
    september_num = 0
    octorber_num = 0
    november_num = 0
    december_num = 0
    for day in range(0,daylen):
        if(daytime[day]!=""):
            d=daytime[day].split("-")
            if (len(d)>=2):
                details = [int(d[0].encode("ascii")), int(d[1].encode("ascii")), int(d[2].encode("ascii"))]
                if(details[1]==9 or (details[1]==10 and details[2]<=5)):
                    september_num= september_num+1
                    print "九月"
                if((details[1]==10 and details[2]>5) or (details[1]==11 and details[2]<=5)):
                    octorber_num= octorber_num+1
                    print "十月"
                if((details[1]==11 and details[2]>5) or (details[1]==12 and details[2]<=5)):
                    november_num= november_num+1
                    print "十一月"

    print "semptember"+bytes(september_num)


timetype()