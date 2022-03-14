# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:30:07 2022
1000以内的完数
@author: MJW
"""
#所有因子的和为因子的乘积
def isws(n): #判断一个数是不是完数
    s = 0
    tag = False
    for i in range(1,n):
        if n % i == 0:
            s += i
    if s == n:
        tag = True
    return tag
if __name__ == "__main__":
    print("1000以内的完数：")
    for i in range(2,1001):
        if isws(i):
            print(i)