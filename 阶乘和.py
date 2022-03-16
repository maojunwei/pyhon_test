# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:22:06 2022
求1+2!+3!+...+20!的和
@author: MJW
"""

def func(n):
    s=1
    for i in range(1,n+1):
        s *= i
    return s
if __name__ == "__main__":
    n =0
    for i in range(1,21):
        n += func(i)
    print("1+2!+3!+...+20!的和为{}".format(n))    
        