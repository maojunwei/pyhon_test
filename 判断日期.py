# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:46:34 2022
输入某年某月某日，判断这一天是这一年的第几天
@author: MJW
"""
y1 = [1,3,5,7,10,12]
y2 = [4,6,8,9,11]

if __name__ == "__main__":
    d = input("请以'y-m-d'格式输入日期：")
    d1 = d.split("-")
    year = int(d1[0])
    month = int(d1[1])
    day = int(d1[2])
    num = 0
    if month <=2:
        num = (month-1) *31 + day
    else:
        num = 28 + 31 
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            num += 1
        for i in range(3,month):
            if i in y1:
                num += 31
            if i in y2:
                num += 30
        num += day
    print("{0}是这一年的第{1}天".format(d,num))
    
