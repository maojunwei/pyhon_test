# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:28:09 2022
一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下，求它在第十次落地时，共经过多少米？第十次反弹多高？
@author: MJW
"""
def f(n,count):
    s = 0
    for i in range(count):
        s += n
        n /= 2
        s += n
    s -= n
    return s,n
if __name__ == "__main__":
    h,num = f(100,10)
    print("第十次落地时，共经过{0}米,第十次反弹{1}米".format(s,h))