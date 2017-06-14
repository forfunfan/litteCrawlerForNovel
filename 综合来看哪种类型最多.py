#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd
from pyExcelerator import *


###写完这个以后我发现自己就是个傻子 明明可以用变量和for循环做完的简单的事我偏偏手打敲了那么多个字 啊气死我了 不过等会儿关于类型的程序可以用那个方法做。

def timetype():
    wb = xlrd.open_workbook('totalbook1.xlsx')
    sh = wb.sheet_by_index(4)
    daytime = sh.col_values(2)
    daylen = len(daytime)
    first_type = ["原创", "同人"]
    second_type = ["言情", "纯爱", "百合", "女尊", "无CP"]
    third_type = ["近代现代", "古色古香", "架空历史", "幻想未来"]
    forth_type = ["爱情", "武侠", "奇幻", "仙侠", "网游", "传奇", "科幻", "童话", "恐怖", "侦探", "动漫", "影视", "小说", "真人", "其他", "剧情", "轻小说"]
    fifth_type = ["重生", "穿越时空", "随身空间", "种田文", "系统", "情有独钟", "网王", "娱乐圈", "仙侠修真", "末世", "HP", "生子",
                  "综漫", "快穿", "甜文", "强强", "异能", "灵魂转换", "异世大陆", "豪门世家", "虐恋情深", "火影", "清穿", "家教", "宫斗",
                  "英美剧", "青梅竹马", "猎人", "韩娱", "武侠", "都市情缘", "女配", "欢喜冤家", "宫廷侯爵", "天之骄子", "日韩剧", "天作之合",
                  "红楼梦", "性别转换", "女强", "无限流", "奇幻魔幻", "布衣生活", "宅斗", "前世今生", "未来架空", "死神", "破镜重圆", "民国旧影", "机甲",
                  "少女漫", "灵异神怪", "游戏网游", "古穿今", "血族", "黑篮", "西方罗曼", "幻想空间", "美食", "科幻", "少年漫", "年下", "洪荒", "江湖恩怨",
                  "婚恋", "海贼王", "西方名著", "港台剧", "乔装改扮", "近水楼台", "乡村爱情", "平步青云", "现代架空", "制服情缘", "时代奇缘", "异国奇缘",
                  "花季雨季", "因缘邂逅", "恩怨情仇", "报仇雪恨", "阴差阳错", "竞技", "历史剧", "悬疑推理", "网配", "恐怖", "励志人生", "业界精英", "传奇",
                  "相爱相杀", "圣斗士", "穿书", "骑士与剑", "原著向", "爱情战争", "银魂", "七五", "恋爱合约", "边缘恋歌", "古典名著", "三教九流", "七年之痒",
                  "霹雳", "SD", "星际", "商战", "职场", "婆媳", "超级英雄", "爽文", "打脸", "升级流", "女扮男装", "东方玄幻", "西幻", "美娱", "网红",
                  "直播"]
    d = [0] * 4
    firstlen = len(first_type)
    secondlen = len(second_type)
    thirdlen = len(third_type)
    forthlen = len(forth_type)
    fifthlen = len(fifth_type)
    totallen = firstlen * secondlen * thirdlen * forthlen*fifthlen
    type = [0] * totallen
    typenum = [0] * totallen
    typelen = 0
    for i in range(0, firstlen):
        for j in range(0, secondlen):
            for m in range(0, thirdlen):
                for n in range(0, forthlen):
                    for x in range(0,fifthlen):
                        type[typelen] = first_type[i] + "-" + second_type[j] + "-" + third_type[m] + "-" + forth_type[n] +"-"+fifth_type[x]
                        typelen = typelen + 1
    no_any_time = 0
    total_space = 0
    error_num = 0
    aaaa = 0
    for day in range(0, daylen):
        if (daytime[day] != ""):
            daytime1 = daytime[day].split("OOO")
            dd1 = daytime1[0].encode("utf8")
            dd2 = daytime1[1].encode("utf8")
            d1 = dd1.split("-")
            len_d = len(d1)
            if (len_d >= 3):
                d1_0 = d1[0].replace(" ", "")
                d1_3 = d1[3].replace(" ", "")
                d = [d1_0, d1[1], d1[2], d1_3]
                ii = first_type.index(d1_0)
                jj = second_type.index(d1[1])
                if (d1[2] != ''):
                    mm = third_type.index(d1[2])
                    nn = forth_type.index(d1_3)
                    if (dd2.find(" ")!= -1):
                        d2=dd2.split(" ")
                        len_d2=len(d2)
                        for sad1 in range(0,len_d2):
                            for sad in range(0,fifthlen):
                                if(fifth_type[sad] == d2[sad1]):
                                    xx = fifth_type.index(d2[sad1])
                                    total_type_num = ii * secondlen * thirdlen * forthlen*fifthlen  + jj * thirdlen * forthlen*fifthlen  + mm * forthlen*fifthlen  + nn*fifthlen+xx
                                    typenum[total_type_num] = typenum[total_type_num] + 1


            else:
                error_num = error_num + 1
        else:
            total_space = total_space + 1

    for b in range(0, totallen):
        print type[b]

    print "小说类型小于4种" + bytes(total_space)
    print "标签出错" + bytes(error_num)


timetype()

