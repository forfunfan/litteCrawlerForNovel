#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd


def noveltypeofauthormost():
    wb = xlrd.open_workbook(r'D:\totalbook.xlsx')
    sh = wb.sheet_by_index(0)
    first_column = sh.col_values(3)
    second_column = sh.col_values(5)
    booklen = len(first_column)
    tongren_num = 0
    yuanchuang_num = 0
    pinglun_num = 0
    suibi_num = 0
    poetry_num = 0
    script_num = 0
    do_not_know_tongoryuan = 0
    unknowtype = 0
    totally_error = 0
    novel_total = 0
    booktypenull = 0
    novel_weizhi_num = 0
    for booktype in range(0,booklen):
        if(first_column[booktype]!=""):
            typelist = first_column[booktype]
            type = typelist.split("-")
            typelen = len(type)
            # 同人和原创数量比较：
            if (typelen > 1):
                novel_total=novel_total+1
                first_type = type[0].encode('utf8')
                no_space_fist_type = first_type.replace(" ","")
                if(no_space_fist_type == "\n原创"):
                    yuanchuang_num = yuanchuang_num + 1
                    print first_type
                elif(no_space_fist_type == "\n同人"):
                    tongren_num = tongren_num + 1
                    print first_type
                elif (no_space_fist_type == "\n未知"):
                    novel_weizhi_num = novel_weizhi_num + 1
                    print first_type
                else:
                    do_not_know_tongoryuan = do_not_know_tongoryuan + 1
                    print first_type
            elif (typelen == 1):
                first_type = type[0].encode('utf8')
                no_space_fist_type = first_type.replace(" ", "")
                if ( no_space_fist_type== "\n评论"):
                    pinglun_num = pinglun_num + 1
                    print first_type
                elif ( no_space_fist_type == "\n随笔"):
                    suibi_num = suibi_num + 1
                    print first_type
                elif ( no_space_fist_type == "\n诗歌"):
                    poetry_num = poetry_num + 1
                    print first_type
                elif ( no_space_fist_type == "\n剧本"):
                    script_num = script_num + 1
                    print first_type
                elif( no_space_fist_type == "\n未知"):
                    unknowtype = unknowtype + 1
                    print first_type
            else:
                totally_error = totally_error+1
                print type
        else:
            booktypenull = booktypenull + 1

    novel_total = yuanchuang_num + tongren_num
    print "原创数量"+bytes(yuanchuang_num),"同人数量"+bytes(tongren_num),"评论数量"+bytes(pinglun_num),"随笔数量"+bytes(suibi_num),"诗歌数量"+bytes(poetry_num),"剧本数量"+bytes(script_num),"未知"+bytes(unknowtype)
    print "小说总数"+bytes( novel_total)
    print "总数量"+bytes( booklen)
    print "jj抽了没有类型"+bytes( booktypenull)
    print "totally_error"+bytes(totally_error)
    print "不知道是同人还是原创"+bytes(do_not_know_tongoryuan)
    print "是小说，但类型未知"+bytes(novel_weizhi_num)

noveltypeofauthormost()