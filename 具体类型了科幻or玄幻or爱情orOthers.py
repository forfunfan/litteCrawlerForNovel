# -*- coding: UTF-8 -*-
#!/usr/bin/python
import xlrd


def noveltypeofauthormost():
    wb = xlrd.open_workbook('totalbook.xlsx')
    sh = wb.sheet_by_index(0)
    first_column = sh.col_values(3)
    booklen = len(first_column)
    love = 0
    wu_xia = 0
    qi_huan = 0
    xian_xia = 0
    wang_you =0
    chuan_qi = 0
    ke_huan = 0
    tong_hua = 0
    kong_bu = 0
    zhen_tan =0
    dong_man = 0
    ying_shi = 0
    xiao_shuo = 0
    zhen_ren = 0
    qi_ta =0
    ju_qing = 0
    qing_xiao_shuo = 0
    do_not_know_error = 0
    totally_error = 0
    booktypenull = 0
    for booktype in range(0,booklen):
        if (first_column[booktype] != ""):
            typelist = first_column[booktype]
            type = typelist.split("-")
            typelen = len(type)
            # 同人和原创数量比较：
            if (typelen > 1):
                third_type1 = type[3].encode('utf8')
                third_type = third_type1.replace(" ","")
                if(third_type == "爱情"):
                    love = love +1
                elif(third_type == "武侠"):
                    wu_xia = wu_xia + 1
                elif(third_type == "奇幻"):
                    qi_huan = qi_huan + 1
                elif(third_type == "仙侠"):
                    xian_xia = xian_xia + 1
                elif(third_type == "网游"):
                    wang_you = wang_you + 1
                elif(third_type == "传奇"):
                    chuan_qi = chuan_qi + 1
                elif(third_type == "科幻"):
                    ke_huan = ke_huan + 1
                elif(third_type == "童话"):
                    tong_hua = tong_hua + 1
                elif(third_type == "恐怖"):
                    kong_bu = kong_bu + 1
                elif(third_type == "侦探"):
                    zhen_tan = zhen_tan + 1
                elif(third_type == "动漫"):
                    dong_man = dong_man + 1
                elif(third_type == "影视"):
                    ying_shi = ying_shi + 1
                elif(third_type == "小说"):
                    xiao_shuo = xiao_shuo + 1
                elif(third_type == "真人"):
                    zhen_ren = zhen_ren + 1
                elif(third_type == "其他"):
                    qi_ta = qi_ta + 1
                elif(third_type == "剧情"):
                    ju_qing = ju_qing + 1
                elif(third_type == "轻小说"):
                    qing_xiao_shuo = qing_xiao_shuo + 1
                else:
                    do_not_know_error = do_not_know_error +1
            else:
                totally_error = totally_error+1
        else:
            booktypenull = booktypenull + 1

    print "爱情" +bytes(love),"武侠" +bytes(wu_xia),"奇幻" +bytes(qi_huan),"仙侠"+bytes(xian_xia),"网游"+bytes(wang_you),"传奇"+bytes(chuan_qi),"科幻"+bytes(ke_huan),"童话"+bytes(tong_hua),"恐怖"+bytes(kong_bu),"侦探"+bytes(zhen_tan),"动漫"+bytes(dong_man),"影视"+bytes(ying_shi),"小说"+bytes(xiao_shuo),"真人"+bytes(zhen_ren),"其他"+bytes(qi_ta),"剧情"+bytes(ju_qing),"轻小说"+bytes(qing_xiao_shuo)
    print "jj抽了没有类型" +bytes(booktypenull)

noveltypeofauthormost()
