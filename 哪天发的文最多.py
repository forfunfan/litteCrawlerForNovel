#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd
###写完这个以后我发现自己就是个傻子 明明可以用变量和for循环做完的简单的事我偏偏手打敲了那么多个字 啊气死我了 不过等会儿关于类型的程序可以用那个方法做。

def timetype():
    wb = xlrd.open_workbook('totalbook1.xlsx')
    sh= wb.sheet_by_index(3)
    daytime = sh.col_values(5)
    daylen = len(daytime)

    september_num9 = 0
    september_num10 = 0
    september_num11 = 0
    september_num12 = 0
    september_num13 = 0
    september_num14 = 0
    september_num15 = 0
    september_num16 = 0
    september_num17 = 0
    september_num18 = 0
    september_num19 = 0
    september_num20 = 0
    september_num21 = 0
    september_num22 = 0
    september_num23 = 0
    september_num24 = 0
    september_num25 = 0
    september_num26 = 0
    september_num27 = 0
    september_num28 = 0
    september_num29 = 0
    september_num30 = 0
    oct_num1 = 0
    oct_num2 = 0
    oct_num3 = 0
    oct_num4 = 0
    oct_num5 = 0
    oct_num6 = 0
    oct_num7 = 0
    oct_num8 = 0
    oct_num9 = 0
    oct_num10 = 0
    oct_num11 = 0
    oct_num12 = 0
    oct_num13 = 0
    oct_num14 = 0
    oct_num15 = 0
    oct_num16 = 0
    oct_num17 = 0
    oct_num18 = 0
    oct_num19 = 0
    oct_num20 = 0
    oct_num21 = 0
    oct_num22 = 0
    oct_num23 = 0
    oct_num24 = 0
    oct_num25 = 0
    oct_num26 = 0
    oct_num27 = 0
    oct_num28 = 0
    oct_num29 = 0
    oct_num30 = 0
    oct_num31 = 0
    nov_num1 = 0
    nov_num2 = 0
    nov_num3 = 0
    nov_num4 = 0
    nov_num5 = 0
    nov_num6 = 0
    nov_num7 = 0
    nov_num8 = 0
    nov_num9 = 0
    nov_num10 = 0
    nov_num11 = 0
    nov_num12 = 0
    nov_num13 = 0
    nov_num14 = 0
    nov_num15 = 0
    nov_num16 = 0
    nov_num17 = 0
    nov_num18 = 0
    nov_num19 = 0
    nov_num20 = 0
    nov_num21 = 0
    nov_num22 = 0
    nov_num23 = 0
    nov_num24 = 0
    nov_num25 = 0
    nov_num26 = 0
    nov_num27 = 0
    nov_num28 = 0
    nov_num29 = 0
    nov_num30 = 0
    december_num1 = 0
    december_num2 = 0
    december_num3 = 0
    december_num4 = 0
    december_num5 = 0
    december_num6 = 0
    december_num7 = 0
    no_any_time =0
    octorber_num = 0
    november_num = 0
    december_num = 0
    for day in range(0,daylen):
        if(daytime[day]!=""):
            d=daytime[day].split("-")
            if (len(d)>=2):
                details = [d[0].decode("ascii"), d[1].decode("ascii"), d[2].decode("ascii")]
                if(details[1]==u"09"):
                    if (details[2]==u"09"):
                            september_num9 = september_num9 +1
                    elif (details[2]==u"10"):
                            september_num10 =september_num10 +1
                    elif (details[2]==u"11"):
                            september_num11 =september_num11 +1
                    elif (details[2]==u"12"):
                            september_num12 =september_num12 +1                        
                    elif (details[2]==u"13"):
                            september_num13 =september_num13 +1
                    elif (details[2]==u"14"):
                            september_num14 =september_num14 +1                     
                    elif (details[2]==u"15"):
                            september_num15 =september_num15 +1
                    elif (details[2]==u"16"):
                            september_num16 =september_num16 +1
                    elif (details[2]==u"17"):
                            september_num17 =september_num17 +1                        
                    elif (details[2]==u"18"):
                            september_num18 =september_num18 +1
                    elif (details[2]==u"19"):
                            september_num19 =september_num19 +1 
                    elif (details[2]==u"20"):
                            september_num20 =september_num20 +1
                    elif (details[2]==u"21"):
                            september_num21 =september_num21 +1
                    elif (details[2]==u"22"):
                            september_num22 =september_num22 +1                        
                    elif (details[2]==u"23"):
                            september_num23 =september_num23 +1
                    elif (details[2]==u"24"):
                            september_num24 =september_num24 +1                     
                    elif (details[2]==u"25"):
                            september_num25 =september_num25 +1
                    elif (details[2]==u"26"):
                            september_num26 =september_num26 +1
                    elif (details[2]==u"27"):
                            september_num27 =september_num27 +1                        
                    elif (details[2]==u"28"):
                            september_num28 =september_num28 +1
                    elif (details[2]==u"29"):
                            september_num29 =september_num29 +1                     
                    elif (details[2]==u"30"):
                            september_num30 =september_num30 +1 
                elif (details[1]==u"10"):
                        if (details[2]==u"01"):
                                oct_num1 = oct_num1 +1
                        elif (details[2]==u"02"):
                                oct_num2 =oct_num2 +1                        
                        elif (details[2]==u"03"):
                                oct_num3 =oct_num3 +1
                        elif (details[2]==u"04"):
                                oct_num4 =oct_num4 +1                       
                        elif (details[2]==u"05"):
                                oct_num5 =oct_num5 +1
                        elif (details[2]==u"06"):
                                oct_num6 =oct_num6 +1
                        elif (details[2]==u"07"):
                                oct_num7 =oct_num7 +1                        
                        elif (details[2]==u"08"):
                                oct_num8 =oct_num8 +1
                        elif (details[2]==u"09"):
                                oct_num9 =oct_num9 +1
                        elif (details[2]==u"10"):
                                oct_num10 =oct_num10 +1
                        elif (details[2]==u"11"):
                                oct_num11 =oct_num11 +1
                        elif (details[2]==u"12"):
                                oct_num12 =oct_num12 +1                        
                        elif (details[2]==u"13"):
                                oct_num13 =oct_num13 +1
                        elif (details[2]==u"14"):
                                oct_num14 =oct_num14 +1                     
                        elif (details[2]==u"15"):
                                oct_num15 =oct_num15 +1
                        elif (details[2]==u"16"):
                                oct_num16 =oct_num16 +1
                        elif (details[2]==u"17"):
                                oct_num17 =oct_num17 +1                        
                        elif (details[2]==u"18"):
                                oct_num18 =oct_num18 +1
                        elif (details[2]==u"19"):
                                oct_num19 =oct_num19 +1 
                        elif (details[2]==u"20"):
                                oct_num20 =oct_num20 +1
                        elif (details[2]==u"21"):
                                oct_num21 =oct_num21 +1
                        elif (details[2]==u"22"):
                                oct_num22 =oct_num22 +1                        
                        elif (details[2]==u"23"):
                                oct_num23 =oct_num23 +1
                        elif (details[2]==u"24"):
                                oct_num24 =oct_num24 +1                     
                        elif (details[2]==u"25"):
                                oct_num25 =oct_num25 +1
                        elif (details[2]==u"26"):
                                oct_num26 =oct_num26 +1
                        elif (details[2]==u"27"):
                                oct_num27 =oct_num27 +1                        
                        elif (details[2]==u"28"):
                                oct_num28 =oct_num28 +1
                        elif (details[2]==u"29"):
                                oct_num29 =oct_num29 +1                     
                        elif (details[2]==u"30"):
                                oct_num30 =oct_num30 +1 
                        elif (details[2]==u"31"):
                                oct_num31 =oct_num31 +1 
                elif(details[1]==u"11"):
                        if (details[2]==u"01"):
                                nov_num1 = nov_num1 +1
                        elif (details[2]==u"02"):
                                nov_num2 =nov_num2 +1                        
                        elif (details[2]==u"03"):
                                nov_num3 =nov_num3 +1
                        elif (details[2]==u"04"):
                                nov_num4 =nov_num4 +1                       
                        elif (details[2]==u"05"):
                                nov_num5 =nov_num5 +1
                        elif (details[2]==u"06"):
                                nov_num6 =nov_num6 +1
                        elif (details[2]==u"07"):
                                nov_num7 =nov_num7 +1                        
                        elif (details[2]==u"08"):
                                nov_num8 =nov_num8 +1
                        elif (details[2]==u"09"):
                                nov_num9 =nov_num9 +1
                        elif (details[2]==u"10"):
                                nov_num10 =nov_num10 +1
                        elif (details[2]==u"11"):
                                nov_num11 =nov_num11 +1
                        elif (details[2]==u"12"):
                                nov_num12 =nov_num12 +1                        
                        elif (details[2]==u"13"):
                                nov_num13 =nov_num13 +1
                        elif (details[2]==u"14"):
                                nov_num14 =nov_num14 +1                     
                        elif (details[2]==u"15"):
                                nov_num15 =nov_num15 +1
                        elif (details[2]==u"16"):
                                nov_num16 =nov_num16 +1
                        elif (details[2]==u"17"):
                                nov_num17 =nov_num17 +1                        
                        elif (details[2]==u"18"):
                                nov_num18 =nov_num18 +1
                        elif (details[2]==u"19"):
                                nov_num19 =nov_num19 +1 
                        elif (details[2]==u"20"):
                                nov_num20 =nov_num20 +1
                        elif (details[2]==u"21"):
                                nov_num21 =nov_num21 +1
                        elif (details[2]==u"22"):
                                nov_num22 =nov_num22 +1                        
                        elif (details[2]==u"23"):
                                nov_num23 =nov_num23 +1
                        elif (details[2]==u"24"):
                                nov_num24 =nov_num24 +1                     
                        elif (details[2]==u"25"):
                                nov_num25 =nov_num25 +1
                        elif (details[2]==u"26"):
                                nov_num26 =nov_num26 +1
                        elif (details[2]==u"27"):
                                nov_num27 =nov_num27 +1                        
                        elif (details[2]==u"28"):
                                nov_num28 =nov_num28 +1
                        elif (details[2]==u"29"):
                                nov_num29 =nov_num29 +1                     
                        elif (details[2]==u"30"):
                                nov_num30 =nov_num30 +1 
                elif (details[1]==u"12"):
                        if (details[2]==u"01"):
                                december_num1 = december_num1 +1
                        elif (details[2]==u"02"):
                                december_num2 =december_num2 +1                        
                        elif (details[2]==u"03"):
                                december_num3 =december_num3 +1
                        elif (details[2]==u"04"):
                                december_num4 =december_num4 +1                     
                        elif (details[2]==u"05"):
                                december_num5 =december_num5 +1
                        elif (details[2]==u"06"):
                                december_num6 =december_num6 +1
                        elif (details[2]==u"07"):
                                december_num7 =december_num7 +1  
                else:
                        no_any_time = no_any_time +1
    print september_num9 
    print september_num10 
    print september_num11
    print september_num12 
    print september_num13 
    print september_num14 
    print september_num15 
    print september_num16 
    print september_num17 
    print september_num18 
    print september_num19 
    print september_num20 
    print september_num21
    print september_num22  
    print september_num23 
    print september_num24 
    print september_num25 
    print september_num26 
    print september_num27 
    print september_num28 
    print september_num29 
    print september_num30 
    print oct_num1 
    print oct_num2 
    print oct_num3 
    print oct_num4 
    print oct_num5 
    print oct_num6 
    print oct_num7 
    print oct_num8 
    print oct_num9 
    print oct_num10 
    print oct_num11
    print oct_num12 
    print oct_num13 
    print oct_num14 
    print oct_num15 
    print oct_num16 
    print oct_num17 
    print oct_num18 
    print oct_num19 
    print oct_num20 
    print oct_num21
    print oct_num22  
    print oct_num23 
    print oct_num24 
    print oct_num25 
    print oct_num26 
    print oct_num27 
    print oct_num28 
    print oct_num29 
    print oct_num30 
    print oct_num31 
    print nov_num1 
    print nov_num2 
    print nov_num3 
    print nov_num4 
    print nov_num5 
    print nov_num6 
    print nov_num7 
    print nov_num8 
    print nov_num9 
    print nov_num10 
    print nov_num11
    print nov_num12 
    print nov_num13 
    print nov_num14 
    print nov_num15 
    print nov_num16 
    print nov_num17 
    print nov_num18 
    print nov_num19 
    print nov_num20 
    print nov_num21 
    print nov_num22 
    print nov_num23 
    print nov_num24 
    print nov_num25 
    print nov_num26 
    print nov_num27 
    print nov_num28 
    print nov_num29 
    print nov_num30 
    print december_num1 
    print december_num2 
    print december_num3 
    print december_num4 
    print december_num5 
    print december_num6 
    print december_num7 
    print no_any_time   


timetype()
