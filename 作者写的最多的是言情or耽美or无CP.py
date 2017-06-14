#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd


def noveltypeofauthormost():
    wb = xlrd.open_workbook('totalbook.xls')
    sh = wb.sheet_by_index(0)
    first_column = sh.col_values(4)
    booklen = len(first_column)
    bg = 0
    bl = 0
    gl = 0
    nv_zun = 0
    no_cp =0
    do_not_know_error = 0
    totally_error = 0
    booktypenull = 0
    for booktype in range(0,booklen):
        if (first_column[booktype] != ""):
            typelist = first_column[booktype].decode('gb2312')
            type = typelist.split("-")
            typelen = len(type)
            # 同人和原创数量比较：
            if (typelen > 1):
                if(type[1] == u"言情"):
                    bg = bg + 1
                elif(type[1] == u"纯爱"):
                    bl = bl + 1
                elif(type[1] == u"无CP"):
                    no_cp = no_cp + 1
                elif(type[1] == u"百合"):
                    gl = gl + 1
                elif(type[1] == u"女尊"):
                    nv_zun = nv_zun + 1
                else:
                    do_not_know_error = do_not_know_error +1
            else:
                totally_error = totally_error+1
        else:
            booktypenull = booktypenull + 1

    print u"言情"+bg,u"纯爱"+bl,u"无CP"+no_cp,u"百合"+gl,u"女尊"+nv_zun
    print u"jj抽了没有类型" + booktypenull
noveltypeofauthormost()