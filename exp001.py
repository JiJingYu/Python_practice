import numpy as np

def Sn(input_num):
    return np.sum([int(i) for i in str(input_num)])

def calc():
    for i in range(1900, 2007):
        if i+Sn(i)+Sn(Sn(i))==2007:
            print(i)

if __name__=='__main__':
    calc()
