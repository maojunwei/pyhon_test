# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:24:54 2022

@author: MJW
"""

def fun(s):
    m1 = max(s)
    m2 = min(s)
    for i,j in enumerate(m2):
        if m1[i] != j:
            return(m1[:i])
    return(m2)
print(fun(["floe","floce","flomb"]))