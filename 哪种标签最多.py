#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd


###写完这个以后我发现自己就是个傻子 明明可以用变量和for循环做完的简单的事我偏偏手打敲了那么多个字 啊气死我了 不过等会儿关于类型的程序可以用那个方法做。

def timetype():
    wb = xlrd.open_workbook('totalbook1.xlsx')
    sh = wb.sheet_by_index(3)
    daytime = sh.col_values(13)
    daylen = len(daytime)
    #all_type = ["爱情", "武侠", "奇幻", "仙侠", "网游", "传奇", "科幻", "童话", "恐怖", "侦探", "动漫", "影视", "小说", "真人", "其他", "剧情", "轻小说"]
    detail_type = ["重生", "穿越时空", "随身空间", "种田文", "系统", "情有独钟", "网王", "娱乐圈", "仙侠修真", "末世", "HP", "生子",
                   "综漫", "快穿", "甜文", "强强", "异能", "灵魂转换", "异世大陆", "豪门世家", "虐恋情深", "火影", "清穿", "家教", "宫斗",
                   "英美剧", "青梅竹马", "猎人", "韩娱", "武侠", "都市情缘", "女配", "欢喜冤家", "宫廷侯爵", "天之骄子", "日韩剧", "天作之合",
                   "红楼梦", "性别转换", "女强", "无限流", "奇幻魔幻", "布衣生活", "宅斗", "前世今生", "未来架空", "死神", "破镜重圆", "民国旧影", "机甲",
                   "少女漫", "灵异神怪", "游戏网游", "古穿今", "血族", "黑篮", "西方罗曼", "幻想空间", "美食", "科幻", "少年漫", "年下", "洪荒", "江湖恩怨",
                   "婚恋", "海贼王", "西方名著", "港台剧", "乔装改扮", "近水楼台", "乡村爱情", "平步青云", "现代架空", "制服情缘", "时代奇缘", "异国奇缘",
                   "花季雨季", "因缘邂逅", "恩怨情仇", "报仇雪恨", "阴差阳错", "竞技", "历史剧", "悬疑推理", "网配", "恐怖", "励志人生", "业界精英", "传奇",
                   "相爱相杀", "圣斗士", "穿书", "骑士与剑", "原著向", "爱情战争", "银魂", "七五", "恋爱合约", "边缘恋歌", "古典名著", "三教九流", "七年之痒",
                   "霹雳", "SD", "星际", "商战", "职场", "婆媳", "超级英雄", "爽文", "打脸", "升级流", "女扮男装", "东方玄幻", "西幻", "美娱", "网红",
                   "直播"]
    len_tag= len(detail_type)
    type = [0] * len_tag
    for i in range(0, len_tag):
        type[i] = 0
    no_any_time = 0
    total_space = 0
    for day in range(0, daylen):
        if (daytime[day] != ""):
            d = daytime[day].split(" ")
            len_d =len(d)
            if (d!= []):
                for ccc in range(0,len_d):
                    details_tag=d[ccc].encode("utf8")
                    for xxx in range(0, len_tag):
                        if (details_tag == detail_type[xxx]):
                            type[xxx] = type[xxx] + 1
                        else:
                            no_any_time = no_any_time + 1
            else:
                total_space = total_space +1

    for a in range(0, len_tag):
        print type[a]
    for b in range(0, len_tag):
        print detail_type[b]
    print no_any_time
    print total_space


timetype()

