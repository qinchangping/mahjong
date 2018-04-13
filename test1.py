__author__ = 'qcp'
# -*- coding:utf-8 -*-
def f(a):
    aa=a[:]
    aa.remove(a[0])
    #del a[0]
    return aa

a1=[1,2,3]
b=f(a1)
print(b)
print(a1)
#remove和del操作都是在原数组上操作，传入参数也是如此