# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 15:13:09 2022
809*??=800*??+9*?? 其中??代表的两位数, 
809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。
求??代表的两位数，及809*??后的结果。
@author: MJW
"""
if __name__ == "__main__":
    x = 0
    for i in range(10,100):
        if len(str(i*809)) == 4 and len(str(i*8)) == 2 and len(str(i*9)) == 3:
            x = i
            break
    print("??代表的两位数是{0}，及809*??后的结果是{1}".format(x,x*809))
