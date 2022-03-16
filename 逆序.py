# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:27:39 2022
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
@author: MJW
"""

if __name__ == "__main__":
    a = str(input("请输入一个不多月5位的正整数："))
    print("{}是{}位数,逆序为{}".format(a,len(a),a[::-1]))