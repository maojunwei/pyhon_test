# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:38:32 2022
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
@author: MJW
"""

if __name__ == "__main__":
    a = int(input("请输入a的值："))
    n = int(input("多少个数相加："))
    num = 0
    for i in range(n):
        s = str(a) * (i+1)
        num += int(s)
    print(num)
        