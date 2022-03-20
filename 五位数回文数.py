# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:28:09 2022
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
@author: MJW
"""

def f(n):
    if len(n) != 5:
        print("不是五位数")
        
    if n == n[::-1]:
        return True
    return False
if __name__ == "__main__":
    n = input("输入一个五位数：")
    if(f(n.strip())):
        print("是")
    else:
        print("否")
    