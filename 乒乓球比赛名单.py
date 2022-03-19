# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:43:26 2022
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
@author: MJW
"""
# 暴力法x= [a,b,c]，求y
def f(y):
    for i in range(3):
        y1 = []
        for j in range(3):
            for k in range(3):
               if  i != j and j!=k and i != k:
                   y1.extend([y[i],y[j],y[k]])
                   if y1[0] !='x' and y1[2] != 'x' and y1[2] !='z':
                       return y1
                     
        
#递归法求全排列
def func(n,begin,end):
    if begin == end:
        print(n)
    for i in range(begin,end):
        n[i],n[begin] = n[begin],n[i]
        func(n,begin+1,end)
        n[i],n[begin] = n[begin],n[i]
if __name__ == "__main__":
    x = ['a','b','c']
    y = ['x','y','z']
    y1 = f(y)
    print("比赛对应名单为：{0}和{1}".format(x,y1))   
    func(y,0,len(y))