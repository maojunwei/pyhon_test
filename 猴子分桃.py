# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:15:20 2022
3、海滩上有一堆桃子，五只猴子来分。
第一只猴子把这堆桃子平均分为五份，
多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，
又多了一个，它同样把多的一个扔入海中，拿走了一份，
第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
@author: MJW
"""
"""
1、反推法
"""
#def f(x):  
#    temp_x = x
#    flag = True
#    for i in range(5):
#        if(temp_x%4 == 0 ):
#            temp_x = temp_x *5 /4 +1
#        else:
#            flag = False
#            break
#    return flag,temp_x
#     
#        
#if __name__ == "__main__":
#    for i in range(1,10000):
#        flag,num = f(i)
#        if(flag):
#            print("海滩上原来最少有{0}个桃子,第五次划分后剩余{1}个".format(num,i))
#            break
"""
2、递归法
引入计数器，寻找能满足五次划分条件的初始数量
"""
def func(count,num):
    if count == 0: #count次已经分完
        return 1
    elif (num - 1) % 5 != 0:
        return -1
    else:
        num = (num - 1) * 4 / 5 
        return func(count-1,num)
if __name__ == "__main__":
    n = 100
    count = 5
    while(1):
        if func(count,n) == 1:
            print("海滩上原来最少有{0}个桃子".format(n))
            break
        n += 1
        