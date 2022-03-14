# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:06:04 2022
1,2,3,4能组成多少个互不相同且无重复数字的三位数
@author: MJW
"""
if __name__ == "__main__":
    s = []
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if (i != j) and (i != k) and (j != k):
                    s.append(100*i+10*j+k)
    print("1,2,3,4能组成{0}个互不相同且无重复数字的三位数,分别是{1}".format(len(s),s))
        
