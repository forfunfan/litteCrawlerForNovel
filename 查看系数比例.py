#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd
from pyExcelerator import *
import datetime

###写完这个以后我发现自己就是个傻子 明明可以用变量和for循环做完的简单的事我偏偏手打敲了那么多个字 啊气死我了 不过等会儿关于类型的程序可以用那个方法做。

def timetype():
    first_type = [u"\n原创",u"\n同人"]
    second_type = [u"言情",u"纯爱",u"百合",u"女尊",u"无CP"]
    third_type = [u"近代现代",u"古色古香",u"架空历史",u"幻想未来"]
    forth_type = [u"爱情",u"武侠",u"奇幻",u"仙侠",u"网游",u"传奇",u"科幻",u"童话",u"恐怖",u"侦探",u"动漫",u"影视",u"小说",u"真人",u"其他",u"剧情",u"轻小说"]
    fifth_type = [u"重生",u"穿越时空",u"随身空间",u"种田文",u"系统",u"情有独钟",u"网王",u"娱乐圈",u"仙侠修真",u"末世",u"HP",u"生子",
                  u"综漫",u"快穿",u"甜文",u"强强",u"异能",u"灵魂转换",u"异世大陆",u"豪门世家",u"虐恋情深",u"火影",u"清穿",u"家教",u"宫斗",
                  u"英美剧",u"青梅竹马",u"猎人",u"韩娱",u"武侠",u"都市情缘",u"女配",u"欢喜冤家",u"宫廷侯爵",u"天之骄子",u"日韩剧",u"天作之合",
                  u"红楼梦",u"性别转换",u"女强",u"无限流",u"奇幻魔幻",u"布衣生活",u"宅斗",u"前世今生",u"未来架空",u"死神",u"破镜重圆",u"民国旧影",u"机甲",
                  u"少女漫",u"灵异神怪",u"游戏网游",u"古穿今",u"血族",u"黑篮",u"西方罗曼",u"幻想空间",u"美食",u"科幻",u"少年漫",u"年下",u"洪荒",u"江湖恩怨",
                  u"婚恋",u"海贼王",u"西方名著",u"港台剧",u"乔装改扮",u"近水楼台",u"乡村爱情",u"平步青云",u"现代架空",u"制服情缘",u"时代奇缘",u"异国奇缘",
                  u"花季雨季",u"因缘邂逅",u"恩怨情仇",u"报仇雪恨",u"阴差阳错",u"竞技",u"历史剧",u"悬疑推理",u"网配",u"恐怖",u"励志人生",u"业界精英",u"传奇",
                  u"相爱相杀",u"圣斗士",u"穿书",u"骑士与剑",u"原著向",u"爱情战争",u"银魂",u"七五",u"恋爱合约",u"边缘恋歌",u"古典名著",u"三教九流",u"七年之痒",
                  u"霹雳",u"SD",u"星际",u"商战",u"职场",u"婆媳",u"超级英雄",u"爽文",u"打脸",u"升级流",u"女扮男装",u"东方玄幻",u"西幻",u"美娱",u"网红",
                  u"直播"]
    d = [0] * 4
    firstlen = len(first_type)
    secondlen = len(second_type)
    thirdlen = len(third_type)
    forthlen = len(forth_type)
    fifthlen = len(fifth_type)
    totallen = firstlen * secondlen * thirdlen * forthlen*fifthlen
    type = [0] * totallen
    typenum = [0] * totallen
    typerate=[0]*totallen
    typelen = 0
    for i in range(0, firstlen):
        for j in range(0, secondlen):
            for m in range(0, thirdlen):
                for n in range(0, forthlen):
                    for x in range(0,fifthlen):
                        type[typelen] = first_type[i] + "-" + second_type[j] + "-" + third_type[m] + "-" + forth_type[n] +"-"+fifth_type[x]
                        typelen = typelen + 1
    total_space = 0
    error_num = 0
    timeend="2016-12-08 23:59:59"
    wb = xlrd.open_workbook('222.xlsx')
    sh = wb.sheet_by_index(1)
    nrows = sh.nrows
    word=[0]*nrows
    time=[0]*nrows
    scores=[0]*nrows
    comment=[0]*nrows
    collect=[0]*nrows
    rate=[0]*nrows
    qi_wen=0
    qi_wen_total=[0]*15
    ctype = 2  # 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    xf = 0  # 扩展的格式化 (默认是0)
    for i in range(nrows):
        word[i] = sh.row(i)[4].value
        scores[i]=sh.row(i)[6].value
        comment[i]=sh.row(i)[8].value
        collect[i]=sh.row(i)[9].value

        d1=xlrd.xldate.xldate_as_datetime(sh.cell(i,5).value, 0)
       # d1=datetime.datetime(x_d1)
        d2 = datetime.datetime.strptime(timeend, '%Y-%m-%d %H:%M:%S')
        delta = d2 - d1
        timelength=delta.days
        rate_time_word= (timelength//7)*5000
        if(rate_time_word<word[i] and rate_time_word!=0 and word[i]!=0):
            rate[i]=collect[i]/(word[i]*timelength)
            type1 = sh.row(i)[3].value
            type=type1.split("-")
            tag= sh.row(i)[14].value
            if (len(type) >= 3):
                type0 = type[0].replace(" ","")
                type3 = type[3].replace(" ","")
                ii = first_type.index(type0)
                jj = second_type.index(type[1])
                if (type[2] != ''):
                    mm = third_type.index(type[2])
                    nn = forth_type.index(type3)
                    if (tag.find(" ") != -1):
                        tagfinal = tag.split(" ")
                        len_tag = len(tagfinal)
                        for sad1 in range(0, len_tag):
                            for sad in range(0, fifthlen):
                                if (fifth_type[sad] == tagfinal[sad1]):
                                    xx = fifth_type.index(tagfinal[sad1])
                                    total_type_num = ii * secondlen * thirdlen * forthlen * fifthlen + jj * thirdlen * forthlen * fifthlen + mm * forthlen * fifthlen + nn * fifthlen + xx
                                    typenum[total_type_num] = typenum[total_type_num] + 1
                                    typerate[total_type_num]=typerate[total_type_num]+rate[i]
        else:
            rate[i]="弃文"
            qi_wen=qi_wen+1
            qi_wen_num=timelength//7
            for qiwennum in range(1,15):
                if(qi_wen_num == qiwennum):
                    qi_wen_total[qiwennum]=qi_wen_total[qiwennum]+1






    print "每部书收藏的系数"
    for d in  range(0,nrows):
        print rate[d]

    print "每类文收藏系数"
    for c in range(0, totallen):
        print typerate[c]




timetype()

