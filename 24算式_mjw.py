# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:21:00 2022

@author: MJW
"""
ysf = ['+','-','*','/']
kh = ["(",")"]

"""
加括号情况：(错误)
1、两个乘除号，加一个括号    -这种情况可以按位插入括号
2、一个乘除号，第二个位置，加两个括号 -暴力写出表达式
3、一个乘除号，非第二个位置，加一个括号  -暴力写出表达式
"""

def f2(ss): #去重
    a = []
    for i in ss:
        if i not in a:
            a.append(i)
    return a
    
def f1(n,start,end): #全排列
    if start == end:
        ss.append(''.join(n))
#        ss.append(n)
        """
        列表可变，字符、元组不可变，得出一种顺序，列表存入会变顺序!!!!????
        """
#        print(n)
#        ss.append(n)
        print(ss)
        return n
    for i in range(start,end):
        n[start],n[i] = n[i],n[start]
        f1(n,i+1,end)
        n[start],n[i] = n[i],n[start]
        
        
def func(n):
    tag = False
    num = 0      
    for i in ysf:
        for j in ysf:
            for k in ysf:
                try: #暴力遍历所有情况
                    s = (n[0] + i + n[1] + j + n[2] + k + n[3])  # 无括号
                    s1 = ('('+n[0] + i + n[1] + j + n[2] + ')' + k + n[3]) # （a#b#c）#d
                    s11 = (n[0] + i + '('+ n[1] + j + n[2]  + k + n[3]+ ')') # a#(b#c#d)
                    s2 = (n[0] + i +'('+ n[1] + j + n[2] + ')' + k + n[3]) #（a#b） # (c#d)
#                    s2 = (n[0] + i + '('+'('+ n[1] + j + n[2] + ')' + k + n[3] +')')
#                    s22 = (n[0] + i + '('+ n[1] + j +'('+ n[2]  + k + n[3] + ')'+')')
                    if "/0" in s or "/0" in s1 or "/0" in s2:
                        continue
                    if abs(eval(s1) - 24.0) <= 0.01:   #（a#b#c）#d
                        tag = True
                        num += 1
                        print(s1)
                    if abs(eval(s11) - 24.0) <= 0.01:   # a#(b#c#d)
                        tag = True
                        num += 1
                        print(s11)
                    if abs(eval(s2) - 24.0) <= 0.01:    #（a#b） # (c#d)
                        tag = True
                        num += 1
                        print(s2)
#                    if eval(s11) == 24.0:    #不加括号
#                        tag = True
#                        num += 1
#                        print(s11)
#                    if eval(s22) == 24.0:    #不加括号
#                        tag = True
#                        num += 1
#                        print(s22)
                    if abs(eval(s) - 24.0) <= 0.01:    #不加括号
                        tag = True
                        num += 1
                        print(s)
                    else:
                        try:
                            if ('+' in s or '-' in s) and ('*' in s or '/' in s): #加减号和乘除号都有的算式
                                num__jj = s.count('+') + s.count('-')
                                if num__jj == 1:   #一个加减号的算式
                                    wz = s.find('+') + s.find('-')+1 #有一个值为-1
                                    l1 = list(s)
                                    l1.insert(wz-1,kh[0])
                                    l1.insert(wz+3,kh[1])
                                    s = "".join(l1)
                                    if abs(eval(s) - 24.0) <= 0.01:    #1、一个加减号的算式，加一对括号
                                        tag = True
                                        num += 1
                                        print(s)
#                                else:
#                                    wz_cs = s.find('*') + s.find('/')+1  #只有一个乘除号的算式
#                                    if wz_cs == 3 :     #乘除号在第二个位置，需要加两个括号
#                                        l1 = list(s)
#                                        l1.insert(0,kh[0])
#                                        l1.insert(4,kh[1])
#                                        l1.insert(6,kh[0])
#                                        l1.append(kh[1])
#                                        s = "".join(l1)
#                                        if abs(eval(s) - 24.0) <= 1e-10:  
#                                            tag = True
#                                            num += 1
#                                            print(s)
#                                    elif wz_cs == 1 :    #乘除号在第一个位置，加减号相邻，加一个括号
#                                        l1 = list(s)
#                                        l1.insert(2,kh[0])
#                                        l1.append(kh[1])
#                                        s = "".join(l1)
#                                        if abs(eval(s) - 24.0) <= 1e-10:   
#                                            tag = True
#                                            num += 1
#                                            print(s)
#                                    else:                 #乘除号在第三个位置，加减号相邻，加一个括号
#                                        l1 = list(s)
#                                        l1.insert(0,kh[0])
#                                        l1.insert(6,kh[1])
#                                        s = "".join(l1)
#                                        if abs(eval(s) - 24.0) <= 1e-10:    
#                                            tag = True
#                                            num += 1
#                                            print(s)
                        except ZeroDivisionError:    #加括号后可能有/0错误
                            continue      
                except ZeroDivisionError:    #加括号后可能有/0错误
                    continue                       
#                                
    return tag,num

if __name__ == "__main__":
    s = input("请输入四个数，以空格间隔：")
    s1 = s.split(" ")
    ss = []
    f1(s1,0,len(s1))
    num = 0
    
    print(ss)
    ss1 = f2(ss)
    print(ss1)
    for i in ss1:
        i 
        t,nn = func(i)
        num += nn
    if num != 0:
        print("如上，{0}可以组成结果是24的算式，共{1}种组合".format(s1,num))
    else:
        print("{0}不能组成结果是24的算式".format(s1))
    