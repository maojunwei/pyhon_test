# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 18:53:29 2022
2、打印出杨辉三角形（要求打印出10行如下图）。
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1 
1 7 21 35 35 21 7 1 
1 8 28 56 70 56 28 8 1 
1 9 36 84 126 126 84 36 9 1
@author: MJW
"""
def func(x,y):  #返回第i行，第j列的值
    if x == y or y == 1:
        return 1
    else:
        return func(x-1,y) + func(x-1,y-1)

if __name__ == "__main__":
    for i in range(1,11):
        s = ''
        for j in range(i):
            s += str(func(i,j+1))
            s += ' '
        print(s)

